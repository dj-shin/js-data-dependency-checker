from __future__ import annotations
from typing import List, TYPE_CHECKING

from estree.node import Node
if TYPE_CHECKING:
    from estree.modules import ModuleDeclaration
    from estree.statement import Statement


class Program(Node):
    def __init__(self, sourcetype: str, body: List[Statement, ModuleDeclaration]):
        super(Program, self).__init__()
        self.sourceType = sourcetype
        self.body = body
