import xmltodict
from collections import OrderedDict
from BPMN.logger import logger
import re


class BPMNParser():

    def __init__(self) -> None:
        self.priortyfinder = re.compile(r'#(\d+)(.+)?')

    def simple_load(self, file_name: str) -> OrderedDict:
        with open(file_name, "r") as file:
            process = xmltodict.parse(file.read()).get("bpmn:definitions", {}).get("bpmn:process", {})
        return process

    def load(self, file_name: str) -> OrderedDict:
        logger.info(f"started parsing file:{file_name}")
        process = self.simple_load(file_name)
        logger.info(f"Parsing completed starting with checks")
        needed_checks = [self._check_start, self._check_end, self._check_task,
                         self._check_exclusiveGateways, self._check_inclusiveGateways, self._check_parallelGateways]
        for check in needed_checks:
            process = check(process)
        logger.info(f"checking complete {file_name} was sucessfully parsed")
        return process

    def _transform_outgoing(self, outgoing, process):
        logger.debug(f"Transforming outgoing flows :{outgoing}")
        if type(outgoing) == str:
            flow = self.find_flow(process, outgoing)
            name = flow.get("@name", "no_name")
            prio = None
            if m := self.priortyfinder.fullmatch(name):
                prio = int(m.group(1))
                group_2 = m.group(2)
                name = group_2 if group_2 is not None else "no_name"
                name = name.strip()
            return {"@id": outgoing, "@name": name, "@targetRef": flow.get("@targetRef", None), "@priority": prio}
        else:
            for key, flow_id in enumerate(outgoing):
                flow = self.find_flow(process, flow_id)
                name = flow.get("@name", "no_name")
                prio = None
                if m := self.priortyfinder.fullmatch(name):
                    prio = int(m.group(1))
                    group_2 = m.group(2)
                    name = group_2 if group_2 is not None else "no_name"
                    name = name.strip()
                outgoing[key] = {"@id": flow_id, "@name": name, "@targetRef": flow.get("@targetRef", None), "@priority": prio}
        return outgoing

    def _check_start(self, process: OrderedDict) -> OrderedDict:
        logger.info(f"Checking startevent")
        start = process.get("bpmn:startEvent", None)
        assert type(start) == OrderedDict, "No Start Event found or multiple startevents"
        assert start.get("bpmn:incoming", None) is None, "startEvent can't have incoming flows"
        outgoing = start.get("bpmn:outgoing", None)
        assert type(outgoing) == str, "Start Event has mulitple Outgoing events or isn't connected"
        process["bpmn:startEvent"]["bpmn:outgoing"] = self._transform_outgoing(outgoing, process)
        logger.info(f"Checking startevent finished sucessfully")
        return process

    def _check_end(self, process):
        logger.info(f"Checking endevent/s")
        end = process.get("bpmn:endEvent", None)
        assert end is not None, "Process needs an EndEvent!"
        if type(end) == OrderedDict:
            end = [end]
        for el in end:
            assert (el.get("bpmn:outgoing", None)) is None, "EndEvents cant have outgoing flows"
            inc = el.get("bpmn:incoming", None)
            assert type(inc) == str, "EndEvents cant have multiple incoming flows please use a closing Gate"
        logger.info(f"Checking Endevent/s finished sucessfully")
        return process

    def _check_task(self, process: OrderedDict) -> OrderedDict:
        logger.info(f"Checking task/s")
        task = process.get("bpmn:task", None)
        if task is not None and type(task) == OrderedDict:
            assert type(task.get("@name", None)) is not None, "Task needs Name/Operation to be used in any meaningful way lol"
            assert type(task.get("bpmn:incoming", None)) == str, "Tasks needs exactly one incoming flow"
            out = task.get("bpmn:outgoing", None)
            assert type(out) == str, "Task needs exactly one outgoing flow"
            process["bpmn:task"]["bpmn:outgoing"] = self._transform_outgoing(out, process)
        elif type(task) != list:
            return process
        else:
            for i, t in enumerate(task):
                assert type(t.get("@name", None)) is not None, "Task needs Name/Operation to be used in any meaningful way lol"
                assert type(t.get("bpmn:incoming", None)) == str, "Tasks needs exactly one incoming flow"
                out = t.get("bpmn:outgoing", None)
                assert type(out) == str, "Task needs exactly one outgoing flow"
                process["bpmn:task"][i]["bpmn:outgoing"] = self._transform_outgoing(out, process)
        logger.info(f"Checking task/s finished successfully")
        return process

    def _check_Gateways(self, process: OrderedDict, gate_type: str, default_op_closed: str, default_op_open: str, check: bool) -> OrderedDict:
        logger.info(f"Checking {gate_type}/s")
        gateways = process.get(gate_type, None)
        if gateways is None:
            logger.info(f"no {gate_type} found checking successfully")
            return process
        elif type(gateways) == list:
            for key, gateway in enumerate(gateways):
                inc = gateway.get("bpmn:incoming", None)
                out = gateway.get("bpmn:outgoing", None)
                assert (inc is not None or out is not None) and type(inc) != type(out), "gateways should be conncted properly"
                if type(inc) == list:
                    assert type(out) == str, "Closing Gate can't be also an Opening Gate"
                    process[gate_type][key]["@opening"] = False
                    process[gate_type][key]["bpmn:outgoing"] = self._transform_outgoing(out, process)
                    # set default operation
                    if gateway.get("@name", None) is None:
                        process[gate_type][key]["@name"] = default_op_closed
                else:
                    assert type(inc) == str, "Opening Gate can't be also a Closing Gate"
                    process[gate_type][key]["@opening"] = True
                    process[gate_type][key]["bpmn:outgoing"] = self._transform_outgoing(out, process)
                    # set default operation
                    if gateway.get("@name", None) is None:
                        process[gate_type][key]["@name"] = default_op_open

                    if check:
                        default = gateway.get("@default", None)
                        for o in out:
                            assert o.get("@name") != "no_name" or o.get("@id") == default, "Opening Gate needs all outgoing flows to have an Condition or be a default Flow"

        else:
            # determine if opening or closing Gate and see if check if all needed infos are present
            inc = gateways.get("bpmn:incoming", None)
            out = gateways.get("bpmn:outgoing", None)
            assert (inc is not None or out is not None) and type(inc) != type(out), "gateways should be conncted properly"
            if type(inc) == list:
                assert type(out) == str, "Closing Gate can't be also an Opening Gate"
                process[gate_type]["@opening"] = False
                process[gate_type]["bpmn:outgoing"] = self._transform_outgoing(out, process)
                # set default operation
                if gateways.get("@name", None) is None:
                    process[gate_type]["@name"] = default_op_closed
            else:
                assert type(inc) == str, "Opening Gate can't be also a Closing Gate"
                process[gate_type]["@opening"] = True
                process[gate_type]["bpmn:outgoing"] = self._transform_outgoing(out, process)
                # set default operation
                if gateways.get("@name", None) is None:
                    process[gate_type]["@name"] = default_op_open

                if check:
                    default = gateways.get("@default", None)
                    for o in out:
                        assert o.get("@name") != "no_name" or o.get("@id") == default, "Opening Gate needs all outgoing flows to have an Condition or be a default Flow"
        logger.info(f"Checking {gate_type}/s finished successfully")
        return process

    def _check_exclusiveGateways(self, process):
        return self._check_Gateways(process, "bpmn:exclusiveGateway", "passtrough", "check", True)

    def _check_inclusiveGateways(self, process):
        return self._check_Gateways(process, "bpmn:inclusiveGateway", "concat", "splice", True)

    def _check_parallelGateways(self, process):
        return self._check_Gateways(process, "bpmn:parallelGateway", "join", "copy", False)

    def find_flow(self, process, flow_id):
        for flow in process.get("bpmn:sequenceFlow"):
            if flow.get("@id") == flow_id:
                return flow
        return None

    def find_element(self, process, element_id) -> dict:
        for key in process:
            if not key.startswith("@") and key != "bpmn:sequenceFlow":
                if type(process[key]) == list:
                    for count, item in enumerate(process[key]):
                        if process[key][count]["@id"] == element_id:
                            return {"type": key,
                                    "information": process[key][count]}
                else:
                    if process[key]["@id"] == element_id:
                        return {"type": key,
                                "information": process[key]}
        return None
