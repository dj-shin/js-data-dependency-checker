from __future__ import annotations
from typing import List, Optional, TYPE_CHECKING

from estree.functions import Function
from estree.node import Node

if TYPE_CHECKING:
    from estree.expression import Expression
    from estree.identifier import Identifier, Pattern
    from estree.statement import FunctionBody


class Declaration(Node):
    pass


class FunctionDeclaration(Function, Declaration):
    def __init__(self, id_: Identifier, params: List[Pattern], body: FunctionBody, generator: bool, expression: bool,
                 async_: bool):
        super(FunctionDeclaration, self).__init__(id_, params, body, generator, async_, expression)


class VariableDeclarator(Node):
    def __init__(self, id_: Pattern, init: Optional[Expression]):
        super(VariableDeclarator, self).__init__()
        self.id = id_
        self.init = init


class VariableDeclaration(Declaration):
    def __init__(self, declarations: List[VariableDeclarator], kind: str):
        super(VariableDeclaration, self).__init__()
        self.declarations = declarations
        self.kind = kind
