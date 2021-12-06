from nodes.node import Node
import pytest


def test_creation():
    node1: Node = Node(0,"test")
    assert  isinstance(node1, Node)


@pytest.mark.parametrize("node,name", [
    (Node(1,"test"), "test"),
    (Node(2, "blabla"), "blabla")
])

def test_names(node: Node, name: str):
    """dummy test for setup """
    assert node.name == name

# for printing in test look at conftest.py
def test_print(capture_stdout):
    print("this was a print statement")
    assert capture_stdout["stdout"] == "this was a print statement\n"
