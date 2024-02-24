from anytree import AnyNode, RenderTree

import inspect
from typing import Sequence
import collections


def get_subclasses(node: AnyNode):
    """
    Get all subclasses of a given class.

    Args:
    cls (class): The base class to find subclasses for.

    Returns:
    list: A list of subclasses of the given class.
    """
    node_children: list[AnyNode] = []

    for subclass in node.value.__subclasses__():
        # CHECK Reconsider the roles of id, value and name
        subclass_node = AnyNode(
            id=f"{subclass}", value=subclass, name=subclass.__name__, children=[]
        )
        node_children.append(subclass_node)

        if issubclass(subclass, type) and subclass is not object:
            print(f"Skipping metaclass {subclass}")
            continue

        subclass_node.children = get_subclasses(subclass_node)
    return node_children


def list_types_implementing_class(base_class):
    """
    List all types that implement a given class.

    Args:
    base_class (class): The class to find implementations for.

    Returns:
    list: A list of types implementing the specified class.
    """
    subclasses = get_subclasses(base_class)

    implementing_types = [
        subclass for subclass in subclasses if inspect.isclass(subclass.value)
    ]
    return implementing_types


root = AnyNode(id=object, value=object, children=[])
root.children = get_subclasses(root)
implementing_types = list_types_implementing_class(root)
print(implementing_types)
print(RenderTree(root).by_attr("name"))
print(len(implementing_types))  # Direct descendants only (?)
print(len([n for n in RenderTree(root)]))
