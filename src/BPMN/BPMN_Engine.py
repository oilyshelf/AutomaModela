import imp
from BPMN import ExclusiveGateway, InclusiveGateway, ParallelGateway
from BPMN.BPMN_Parser import BPMNParser
import heapq  # priorityque lol
from typing import List
from BPMN.BPMN_Component import BPMNComponent
from BPMN.StrategyFactory import BAF
from BPMN.StartEvent import StartEvent
from BPMN.Task import Task
from BPMN.Endevent import EndEvent


class BPMNEngine():
    def __init__(self,file_name:str):
        self.parser = BPMNParser()
        self.strat_fact = BAF()
        self.process = self.parser.load(file_name)
        self.elements = []
        self.find_start()
    
    def find_start(self):
        start = self.process.get("bpmn:startEvent")
        heapq.heappush(self.elements, (1,StartEvent(start)))
        
    def run(self):
        while self.elements:
            prio,cur = heapq.heappop(self.elements)
            print(prio, cur)
            next_step = cur.execute()
            if next_step["operation"] == "add":
                for element in next_step["elements"]:
                    self.add(element)
            elif next_step["operation"] == "repush":
                print(f"{cur} was repushed with prio: {prio+1}")
                heapq.heappush(self.elements, (prio+1, cur))
            elif next_step["operation"] == "end":
                if len(self.elements) == 0:
                    print("Process ended")
            else:
                pass
    def add(self, next_element):
        #check if element is already in queue
        for prio, el in self.elements:
            if el.id == next_element["id"]:
                el_type = type(el)
                if el_type == ParallelGateway or el_type == ExclusiveGateway or el_type == InclusiveGateway:
                    el.token.append(next_element["token"])
                return
        element = self.parser.find_element(self.process, next_element["id"])
        # print(element)
        if element["type"] == "bpmn:task":
            heapq.heappush(self.elements,(1,Task(element["information"], next_element["token"], self.strat_fact)))
        elif element["type"] == "bpmn:exclusiveGateway":
            heapq.heappush(self.elements, (5,ExclusiveGateway(element["information"], next_element["token"])))
        elif element["type"] == "bpmn:parallelGateway":
            heapq.heappush(self.elements, (5,ParallelGateway(element["information"], next_element["token"])))
        elif element["type"] == "bpmn:inclusiveGateway":
            heapq.heappush(self.elements, (5,InclusiveGateway(element["information"], next_element["token"])))
        elif element["type"] == "bpmn:endEvent":
            heapq.heappush(self.elements, (10,EndEvent(element["information"], next_element["token"])))
        else:
            pass
        
        
        