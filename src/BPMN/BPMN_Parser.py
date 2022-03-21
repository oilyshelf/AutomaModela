import xmltodict
import json


class BPMNParser():
    def load(self, bpmn_filepath):
        final_definition = {}
        json_process_definition = xmltodict.parse(bpmn_filepath)
        return json.loads(json.dumps(json_process_definition.get("bpmn:definitions", {}).get("bpmn:process", {})))
