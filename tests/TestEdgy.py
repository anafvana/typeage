from tests.TestChild import TestChild
from tests.TestGrandchild import TestGrandchild


class TestEdgy(TestGrandchild, TestChild):
    pass
