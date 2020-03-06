from __future__ import annotations
from typing import Optional, List, TYPE_CHECKING

from estree.node import Node
from estree.declarations import Declaration
from estree.expression import Expression

if TYPE_CHECKING:
    from estree.expression import FunctionExpression
    from estree.identifier import Identifier


class MethodDefinition(Node):
    def __init__(self, key: Expression, value: FunctionExpression, kind: str, computed: bool, static: bool):
        super(MethodDefinition, self).__init__()
        self.key = key
        self.value = value
        self.kind = kind
        self.computed = computed
        self.static = static


class ClassBody(Node):
    def __init__(self, body: List[MethodDefinition]):
        super(ClassBody, self).__init__()
        self.body = body


class Class(Node):
    def __init__(self, id_: Optional[Identifier], superclass: Optional[Expression], body: ClassBody):
        super(Class, self).__init__()
        self.id = id_
        self.superClass = superclass
        self.body = body


class ClassDeclaration(Class, Declaration):
    def __init__(self, id_: Identifier, superclass: Optional[Expression], body: ClassBody):
        super(ClassDeclaration, self).__init__(id_, superclass, body)


class ClassExpression(Class, Expression):
    pass


class MetaProperty(Expression):
    def __init__(self, meta: Identifier, property_: Identifier):
        super(MetaProperty, self).__init__()
        self.meta = meta
        self.property = property_
