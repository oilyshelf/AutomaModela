from nodes.node import Node


def test_nodes():
    """dummy test for setup """
    node1:Node = Node(1, "child")
    node2:Node = Node(2, "parent", [1])
    assert node1.name == "child"
    assert node2.name == "parent"
    assert node1 is not node2
