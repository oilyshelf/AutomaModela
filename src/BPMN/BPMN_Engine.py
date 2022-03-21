import imp
from .BPMN_Parser import BPMNParser
import heapq  # priorityque lol
from typing import List
from .BPMN_Component import BPMNComponent


class BPMNEngine():
    parser: BPMNParser
    elements: List[BPMNComponent]
