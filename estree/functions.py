from __future__ import annotations
from typing import Optional, List, TYPE_CHECKING

from estree.node import Node

if TYPE_CHECKING:
    from estree.identifier import Identifier, Pattern
    from estree.statement import FunctionBody


class Function(Node):
    def __init__(self, id_: Optional[Identifier], params: List[Pattern], body: FunctionBody, generator: bool,
                 async_: bool, expression: bool):
        super(Function, self).__init__()
        self.id = id_
        self.params = params
        self.body = body
        self.generator = generator
        self.async_ = async_
        self.expression = expression
