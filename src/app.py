import os
# import sys
from BPMN import BPMNEngine, logger
from time import perf_counter


def main():
    start = perf_counter()
    os.chdir("./UseCases/ICR")
    engine = BPMNEngine("icr.bpmn")
    end_1 = perf_counter()
    engine.run()
    end_2 = perf_counter()
    logger.info(f"Execution took {end_2-start} seconds (Prep Time: {end_1-start}s and Execution Time: {end_2-end_1} )")


if __name__ == "__main__":
    main()
