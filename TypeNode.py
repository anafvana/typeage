from anytree import AnyNode


class TypeNode(AnyNode):
    id: str = None
    value: type = None
    name: str = None
    children: list = None

    def __init__(self, value: type, id: str | None = None, **kwargs):
        super().__init__(**kwargs)
        self.value = value
        self.id = str(value) if id is None else id
        self.name = value.__name__
        self.children = [TypeNode(value=subclass) for subclass in value.__subclasses__()]

    def __eq__(self, other):
        if isinstance(other, AnyNode):
            if hasattr(other, "value"):
                return self.value == other.value
        return False

    def __hash__(self):
        return hash(self.value)
