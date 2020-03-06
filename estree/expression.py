from __future__ import annotations
from typing import List, Optional, Union, TYPE_CHECKING

from estree.patterns import Pattern
from estree.node import Node
from estree.functions import Function

if TYPE_CHECKING:
    from estree.identifier import Identifier
    from estree.statement import FunctionBody


class Expression(Node):
    pass


class Super(Node):
    pass


class ThisExpression(Expression):
    pass


class SpreadElement(Node):
    def __init__(self, argument: Expression):
        super(SpreadElement, self).__init__()
        self.argument = argument


class ArrayExpression(Expression):
    def __init__(self, elements: List[Optional[Union[Expression, SpreadElement]]]):
        super(ArrayExpression, self).__init__()
        self.elements = elements


class Property(Node):
    def __init__(self, key: Expression, value: Union[Expression, Pattern], kind: str, method: bool, shorthand: bool,
                 computed: bool):
        super(Property, self).__init__()
        self.key = key
        self.value = value
        self.kind = kind
        self.method = method
        self.shorthand = shorthand
        self.computed = computed


class AssignmentProperty(Property):
    def __init__(self, key: Expression, value: Pattern, shorthand: bool, computed: bool):
        super(AssignmentProperty, self).__init__(key=key, value=value, kind='init', method=False, shorthand=shorthand,
                                                 computed=computed)


class ObjectExpression(Expression):
    def __init__(self, properties: List[Property]):
        super(ObjectExpression, self).__init__()
        self.properties = properties


class FunctionExpression(Function, Expression):
    def __init__(self, id_: Optional[Identifier], params: List[Pattern], body: FunctionBody, generator: bool,
                 async_: bool, expression: bool):
        super(FunctionExpression, self).__init__(id_, params, body, generator, async_, expression)


class UnaryExpression(Expression):
    def __init__(self, operator: str, prefix: bool, argument: Expression):
        super(UnaryExpression, self).__init__()
        self.operator = operator
        self.prefix = prefix
        self.argument = argument


class UpdateExpression(Expression):
    def __init__(self, operator: str, argument: Expression, prefix: bool):
        super(UpdateExpression, self).__init__()
        self.operator = operator
        self.argument = argument
        self.prefix = prefix


class BinaryExpression(Expression):
    def __init__(self, operator: str, left: Expression, right: Expression):
        super(BinaryExpression, self).__init__()
        self.operator = operator
        self.left = left
        self.right = right


class AssignmentExpression(Expression):
    def __init__(self, operator: str, left: Pattern, right: Expression):
        super(AssignmentExpression, self).__init__()
        self.operator = operator
        self.left = left
        self.right = right


class LogicalExpression(Expression):
    def __init__(self, operator: str, left: Union[Pattern, Expression], right: Expression):
        super(LogicalExpression, self).__init__()
        self.operator = operator
        self.left = left
        self.right = right


class MemberExpression(Expression, Pattern):
    def __init__(self, object_: [Expression, Super], property_: Expression, computed: bool):
        super(MemberExpression, self).__init__()
        self.object = object_
        self.property = property_
        self.computer = computed


class ConditionalExpression(Expression):
    def __init__(self, test: Expression, alternate: Expression, consequent: Expression):
        super(ConditionalExpression, self).__init__()
        self.test = test
        self.alternate = alternate
        self.consequent = consequent


class CallExpression(Expression):
    def __init__(self, callee: Union[Expression, Super], arguments: List[Union[Expression, SpreadElement]]):
        super(CallExpression, self).__init__()
        self.callee = callee
        self.arguments = arguments


class NewExpression(Expression):
    def __init__(self, callee: Expression, arguments: List[Union[Expression, SpreadElement]]):
        super(NewExpression, self).__init__()
        self.callee = callee
        self.arguments = arguments


class SequenceExpression(Expression):
    def __init__(self, expressions: List[Expression]):
        super(SequenceExpression, self).__init__()
        self.expressions = expressions


class ArrowFunctionExpression(Function, Expression):
    def __init__(self, id_: Optional[Identifier], params: List[Pattern], body: Union[FunctionBody, Expression],
                 generator: bool, expression: bool, async_: bool):
        super(ArrowFunctionExpression, self).__init__(id_, params, body, generator, async_, expression)


class YieldExpression(Expression):
    def __init__(self, argument: Optional[Expression], delegate: bool):
        super(YieldExpression, self).__init__()
        self.argument = argument
        self.delegate = delegate


class AwaitExpression(Expression):
    def __init__(self, argument: Expression):
        super(AwaitExpression, self).__init__()
        self.argument = argument
