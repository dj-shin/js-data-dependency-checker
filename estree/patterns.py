from __future__ import annotations
from estree.node import Node
from typing import List, Optional, TYPE_CHECKING


if TYPE_CHECKING:
    from estree.expression import AssignmentProperty
    from estree.expression import Expression


class Pattern(Node):
    pass


class ObjectPattern(Pattern):
    def __init__(self, properties: List[AssignmentProperty]):
        super(ObjectPattern, self).__init__()
        self.properties = properties


class ArrayPattern(Pattern):
    def __init__(self, elements: List[Optional[Pattern]]):
        super(ArrayPattern, self).__init__()
        self.elements = elements


class RestElement(Pattern):
    def __init__(self, argument: Pattern):
        super(RestElement, self).__init__()
        self.argument = argument


class AssignmentPattern(Pattern):
    def __init__(self, left: Pattern, right: Expression):
        super(AssignmentPattern, self).__init__()
        self.left = left
        self.right = right
