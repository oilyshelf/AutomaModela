from BPMN import ExclusiveGateway, InclusiveGateway, ParallelGateway
from BPMN.BPMN_Parser import BPMNParser
import heapq  # priorityque lol
from typing import List
from BPMN.BPMN_Component import BPMNComponent
from BPMN.StrategyFactory import TSF
from BPMN.StartEvent import StartEvent
from BPMN.Task import Task
from BPMN.Endevent import EndEvent
from BPMN.logger import logger


class BPMNEngine():
    def __init__(self, file_name: str,parser= None, strategy_factory=None):
        self.parser = BPMNParser() if parser is None else parser
        self.name = file_name
        try:
            self.process = self.parser.load(file_name)
        except AssertionError as e:
            logger.error(f"Parsing of Process {file_name} failed due to {e.with_traceback}")

        self.strat_fact = TSF() if strategy_factory is None else strategy_factory
        self.elements: List[BPMNComponent] = []
        self.find_start()

    def find_start(self):
        start = self.process.get("bpmn:startEvent")
        heapq.heappush(self.elements, (1, StartEvent(start)))
        logger.info("Found startevent and added it to the queue")

    def run(self):
        logger.info(f"starting process from {self.name}")
        while self.elements:
            prio, cur = heapq.heappop(self.elements)
            logger.info(f"Next Element in queue is {cur} with the priority of {prio}")
            next_step = cur.execute()
            if next_step["operation"] == "add":
                for element in next_step["elements"]:
                    self.add(element)
            elif next_step["operation"] == "repush":
                logger.info(f"{cur} was repushed with prio: {prio + 1}")
                heapq.heappush(self.elements, (prio + 1, cur))
            elif next_step["operation"] == "end":
                if len(self.elements) == 0:
                    logger.info(f"Process ended successfully no more elements in the queue")
            else:
                pass

    def add(self, next_element):
        # check if element is already in queue
        for prio, el in self.elements:
            if el.id == next_element["id"]:
                el_type = type(el)
                if el_type == ParallelGateway or el_type == ExclusiveGateway or el_type == InclusiveGateway:
                    el.token.append(next_element["token"])
                    logger.info(f"{str(el)} already in queue token added to it")
                return
        element = self.parser.find_element(self.process, next_element["id"])
        # logger.info(element)
        if element["type"] == "bpmn:task":
            heapq.heappush(self.elements, (1, Task(element["information"], next_element["token"], self.strat_fact)))
        elif element["type"] == "bpmn:exclusiveGateway":
            heapq.heappush(self.elements, (5, ExclusiveGateway(element["information"], next_element["token"])))
        elif element["type"] == "bpmn:parallelGateway":
            heapq.heappush(self.elements, (5, ParallelGateway(element["information"], next_element["token"])))
        elif element["type"] == "bpmn:inclusiveGateway":
            heapq.heappush(self.elements, (5, InclusiveGateway(element["information"], next_element["token"])))
        elif element["type"] == "bpmn:endEvent":
            heapq.heappush(self.elements, (10, EndEvent(element["information"], next_element["token"])))
        else:
            logger.warning(f'{element["type"]} is unknown no element created')
            return
        logger.info(f"Element of type {element['type']} : {element['information']} created and added to the queue")
