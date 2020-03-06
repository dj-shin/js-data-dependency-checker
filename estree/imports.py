from __future__ import annotations
from typing import List, Union, TYPE_CHECKING

from estree.modules import ModuleDeclaration, ModuleSpecifier

if TYPE_CHECKING:
    from estree.identifier import Identifier
    from estree.literal import Literal


class ImportSpecifier(ModuleSpecifier):
    def __init__(self, local: Identifier, imported: Identifier):
        super(ImportSpecifier, self).__init__(local)
        self.imported = imported


class ImportDefaultSpecifier(ModuleSpecifier):
    pass


class ImportNamespaceSpecifier(ModuleSpecifier):
    pass


class ImportDeclaration(ModuleDeclaration):
    def __init__(self, specifiers: List[Union[ImportSpecifier, ImportDefaultSpecifier, ImportNamespaceSpecifier]],
                 source: Literal):
        super(ImportDeclaration, self).__init__()
        self.specifiers = specifiers
        self.source = source
