from __future__ import annotations

from estree.expression import Expression
from estree.patterns import Pattern


class Identifier(Expression, Pattern):
    def __init__(self, name: str):
        super(Identifier, self).__init__()
        self.name = name
