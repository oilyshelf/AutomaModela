import os
# import sys
from BPMN import BPMNEngine


def main():
    os.chdir("./Notebooks")
    engine = BPMNEngine("inkltest.bpmn")
    engine.run()


if __name__ == "__main__":
    main()
