from __future__ import annotations
from typing import List, Union, Optional, TYPE_CHECKING

from estree.node import Node

if TYPE_CHECKING:
    from estree.declarations import VariableDeclaration
    from estree.identifier import Identifier, Pattern
    from estree.literal import Literal
    from estree.expression import Expression


class Statement(Node):
    pass


class ExpressionStatement(Statement):
    def __init__(self, expression: Expression):
        super(ExpressionStatement, self).__init__()
        self.expression = expression


class Directive(Node):
    def __init__(self, expression: Literal, directive: str):
        super(Directive, self).__init__()
        self.expression = expression
        self.directive = directive


class BlockStatement(Statement):
    def __init__(self, body: List[Statement]):
        super(BlockStatement, self).__init__()
        self.body = body


class FunctionBody(Statement):
    def __init__(self, body: List[Union[Directive, Statement]]):
        super(FunctionBody, self).__init__()
        self.body = body


class EmptyStatement(Statement):
    def __init__(self):
        super(EmptyStatement, self).__init__()


class DebuggerStatement(Statement):
    def __init__(self):
        super(DebuggerStatement, self).__init__()


class WithStatement(Statement):
    def __init__(self, object_: Expression, body: Statement):
        super(WithStatement, self).__init__()
        self.object = object_
        self.body = body


class ReturnStatement(Statement):
    def __init__(self, argument: Optional[Expression]):
        super(ReturnStatement, self).__init__()
        self.argument = argument


class LabeledStatement(Statement):
    def __init__(self, label: Identifier, body: Statement):
        super(LabeledStatement, self).__init__()
        self.label = label
        self.body = body


class BreakStatement(Statement):
    def __init__(self, label: Optional[Identifier]):
        super(BreakStatement, self).__init__()
        self.label = label


class ContinueStatement(Statement):
    def __init__(self, label: Optional[Identifier]):
        super(ContinueStatement, self).__init__()
        self.label = label


class IfStatement(Statement):
    def __init__(self, test: Expression, consequent: Statement, alternate: Optional[Statement]):
        super(IfStatement, self).__init__()
        self.test = test
        self.consequent = consequent
        self.alternate = alternate


class SwitchCase(Node):
    def __init__(self, test: Optional[Expression], consequent: List[Statement]):
        super(SwitchCase, self).__init__()
        self.test = test
        self.consequent = consequent


class SwitchStatement(Statement):
    def __init__(self, discriminant: Expression, cases: List[SwitchCase]):
        super(SwitchStatement, self).__init__()
        self.discriminant = discriminant
        self.cases = cases


class ThrowStatement(Statement):
    def __init__(self, argument: Expression):
        super(ThrowStatement, self).__init__()
        self.argument = argument


class CatchClause(Node):
    def __init__(self, param: Pattern, body: BlockStatement):
        super(CatchClause, self).__init__()
        self.param = param
        self.body = body


class TryStatement(Statement):
    def __init__(self, block: BlockStatement, handler: Optional[CatchClause], finalizer: Optional[BlockStatement]):
        super(TryStatement, self).__init__()
        self.block = block
        self.handler = handler
        self.finalizer = finalizer


class WhileStatement(Statement):
    def __init__(self, test: Expression, body: Statement):
        super(WhileStatement, self).__init__()
        self.test = test
        self.body = body


class DoWhileStatement(Statement):
    def __init__(self, body: Statement, test: Expression):
        super(DoWhileStatement, self).__init__()
        self.body = body
        self.test = test


class ForStatement(Statement):
    def __init__(self, init: Optional[Union[VariableDeclaration, Expression]], test: Optional[Expression],
                 update: Optional[Expression], body: Statement):
        super(ForStatement, self).__init__()
        self.init = init
        self.test = test
        self.update = update
        self.body = body


class ForInStatement(Statement):
    def __init__(self, left: Union[VariableDeclaration, Pattern], right: Expression, body: Statement):
        super(ForInStatement, self).__init__()
        self.left = left
        self.right = right
        self.body = body


class ForOfStatement(ForInStatement):
    def __init__(self, left: Union[VariableDeclaration, Pattern], right: Expression, body: Statement, await_: bool):
        super(ForOfStatement, self).__init__(left, right, body)
        self.await_ = await_
