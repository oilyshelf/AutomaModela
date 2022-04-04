from BPMN.BPMN_Parser import BPMNParser
import pytest


def test_load():
    parser = BPMNParser()
    assert type(parser) == BPMNParser, "dummer test"

# for printing in test look at conftest.py


def test_print(capture_stdout):
    print("this was a print statement")
    assert capture_stdout["stdout"] == "this was a print statement\n"
