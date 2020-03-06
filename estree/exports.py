from __future__ import annotations
from typing import Optional, List, Union, Pattern, TYPE_CHECKING

from estree.modules import ModuleDeclaration, ModuleSpecifier
from estree.classes import Class
from estree.functions import Function

if TYPE_CHECKING:
    from estree.classes import ClassBody, ClassDeclaration
    from estree.declarations import Declaration, FunctionDeclaration
    from estree.expression import Expression
    from estree.identifier import Identifier
    from estree.literal import Literal
    from estree.statement import FunctionBody


class ExportSpecifier(ModuleSpecifier):
    def __init__(self, local: Identifier, exported: Identifier):
        super(ExportSpecifier, self).__init__(local)
        self.exported = exported


class ExportNamedDeclaration(ModuleDeclaration):
    def __init__(self, declarations: Optional[Declaration], specifiers: List[ExportSpecifier],
                 source: Optional[Literal]):
        super(ExportNamedDeclaration, self).__init__()
        self.declarations = declarations
        self.specifiers = specifiers
        self.source = source


class AnonymousDefaultExportedFunctionDeclaration(Function):
    def __init__(self, params: List[Pattern], body: FunctionBody, generator: bool, async_: bool):
        super(AnonymousDefaultExportedFunctionDeclaration, self).__init__(id_=None, params=params, body=body,
                                                                          generator=generator, async_=async_)


class AnonymousDefaultExportedClassDeclaration(Class):
    def __init__(self, superclass: Optional[Expression], body: ClassBody):
        super(AnonymousDefaultExportedClassDeclaration, self).__init__(id_=None, superclass=superclass, body=body)


class ExportDefaultDeclaration(ModuleDeclaration):
    def __init__(self, declaration: Union[AnonymousDefaultExportedFunctionDeclaration,
                                          AnonymousDefaultExportedFunctionDeclaration,
                                          FunctionDeclaration, ClassDeclaration, Expression]):
        super(ExportDefaultDeclaration, self).__init__()
        self.declaration = declaration


class ExportAllDeclaration(ModuleDeclaration):
    def __init__(self, source: Literal):
        super(ExportAllDeclaration, self).__init__()
        self.source = source
