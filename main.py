from anytree import AnyNode, RenderTree  # type: ignore

import inspect
from typing import Sequence
import collections

from TypeNode import TypeNode


def get_subclasses(node: TypeNode) -> list[TypeNode]:
    """
    Get all subclasses of a given class.

    Args:
    cls (class): The base class to find subclasses for.

    Returns:
    list: A list of subclasses of the given class.
    """
    node_children: list[TypeNode] = []

    for subclass in node.value.__subclasses__():
        # CHECK Reconsider the roles of id, value and name; N.B.: id is always string
        subclass_node = TypeNode(
            id=f"{subclass}", value=subclass, name=subclass.__name__, children=[]
        )
        node_children.append(subclass_node)

        if issubclass(subclass, type) and subclass is not object:
            print(f"Skipping metaclass {subclass}")
            continue

        subclass_node.children = get_subclasses(subclass_node)
    return node_children


def flatten_tree(node: TypeNode, flat_tree: set = None) -> set[TypeNode]:
    if flat_tree is None:
        flat_tree = set()

    if node not in flat_tree:
        flat_tree.add(node)

    if node.children:
        for child in node.children:
            flatten_tree(child, flat_tree)

    return flat_tree


def flatten(node: TypeNode, flat_tree: set = None) -> set[type]:
    if flat_tree is None:
        flat_tree = set()

    if node not in flat_tree:
        flat_tree.add(node.value)

    subclasses = node.value.__subclasses__()
    if subclasses:
        for subclass in subclasses:
            flatten(TypeNode(value=subclass), flat_tree)

    return flat_tree


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


# root = TypeNode(id=object, value=object, children=[])
# root.children = get_subclasses(root)
# implementing_types = list_types_implementing_class(root)
# print(implementing_types)
# print(RenderTree(root).by_attr("name"))
# print(len(implementing_types))  # Direct descendants only (?)
# print(len([n for n in RenderTree(root)]))
# print(flatten(RenderTree(root)))

# root = AnyNode(id=object, value=object, children=[])
# root.children = get_subclasses(root)
# implementing_types = list_types_implementing_class(root)
# print(implementing_types)
# print(RenderTree(root).by_attr("name"))
# print(len(implementing_types))  # Direct descendants only (?)
# print(len([n for n in RenderTree(root)]))
# print(flatten(RenderTree(root)))
