from __future__ import annotations
from estree.node import Node
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from estree.identifier import Identifier


class ModuleDeclaration(Node):
    def __init__(self):
        super(ModuleDeclaration, self).__init__()


class ModuleSpecifier(Node):
    def __init__(self, local: Identifier):
        super(ModuleSpecifier, self).__init__()
        self.local = local
