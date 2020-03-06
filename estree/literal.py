from __future__ import annotations
from typing import List, Dict

from estree.expression import Expression
from estree.node import Node


class Literal(Expression):
    def __init__(self, value: List[str, bool, None, int, float]):
        super(Literal, self).__init__()
        self.value = value


class RegExpLiteral(Literal):
    def __init__(self, value: List[str, bool, None, int, float], regex: Dict[str, str]):
        super(RegExpLiteral, self).__init__(value)
        self.regex = regex


class TemplateElement(Node):
    def __init__(self, tail: bool, value: Dict[str, str]):
        super(TemplateElement, self).__init__()
        self.tail = tail
        self.value = value


class TemplateLiteral(Expression):
    def __init__(self, quasis: List[TemplateElement], expressions: List[Expression]):
        super(TemplateLiteral, self).__init__()
        self.quasis = quasis
        self.expressions = expressions
