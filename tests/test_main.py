from anytree import RenderTree

from TestEdgy import TestEdgy
from TypeNode import TypeNode
from main import get_subclasses, flatten
from tests.TestGrandchild import TestGrandchild
from tests.TestChild import TestChild
from tests.TestRoot import TestRoot

root = TypeNode(value=TestRoot)
child = TypeNode(value=TestChild, id="ARandomID")
grandchild = TypeNode(value=TestGrandchild)
edgy = TypeNode(value=TestEdgy)

def test_TypeNode():
    # TypeNode.__init__
    assert root.value == TestRoot
    assert root.id == str(TestRoot)
    assert root.name == "TestRoot"
    assert root.children == [child]

    child_index = root.children.index(child)
    assert child_index > -1
    #FIXME How to handle this?
    assert root.children[child_index].id == child.id

    # TypeNode.__eq__
    assert root == TypeNode(value=TestRoot)

    # TypeNode.children
    assert root.children[child_index] == child
    assert root.children[child_index].value == TestChild
    assert (grandchild in root.children[child_index].children) == True

    # TypeNode.__hash__
    root_set = {TypeNode(value=TestRoot)}
    root_set.add(root)
    assert root_set == {TypeNode(value=TestRoot)}


def test_get_subclasses():
    assert get_subclasses(root) == [TypeNode(value=TestChild)]
    assert get_subclasses(root) != [TypeNode(value=TestGrandchild)]


def test_flatten():
    assert flatten(root) == {TestRoot, TestChild, TestGrandchild, TestEdgy}


def test_tree():
    tree = RenderTree(root).by_attr("name")
    print()
    print(tree)

# r = TypeNode(
#     id="r",
#     value="r",
#     name="r",
#     children=[
#         TypeNode(
#             id="ra",
#             value="ra",
#             name="ra",
#             children=[
#                 TypeNode(id="ra1", value="ra1", name="ra1"),
#                 TypeNode(id="ra2", value="ra2", name="ra2"),
#             ],
#         ),
#         TypeNode(
#             id="rb",
#             value="rb",
#             name="rb",
#             children=[
#                 TypeNode(id="rb1", value="rb1", name="rb1"),
#                 TypeNode(id="ra2", value="ra2", name="ra2"),
#             ],
#         ),
#     ],
# )

# print(RenderTree(r).by_attr("name"))
# print(len([n for n in RenderTree(r)]))
# print(flatten(RenderTree(r)))
