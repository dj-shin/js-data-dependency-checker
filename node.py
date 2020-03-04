from statement import Statement
from statement import VariableDeclaration
from statement import VariableDeclarator
from statement import FunctionDeclaration
from statement import ClassDeclaration
from statement import ClassBody
from statement import BlockStatement
from statement import MethodDefinition
from statement import ReturnStatement
from statement import ExpressionStatement
from statement import IfStatement
from statement import BreakStatement
from statement import ContinueStatement
from statement import SwitchStatement
from statement import SwitchCase
from statement import TryStatement
from statement import ForStatement
from statement import WhileStatement
from statement import ForOfStatement
from statement import ForInStatement
from statement import CatchClause
from statement import EmptyStatement
from statement import LabeledStatement

from statement import ArrowFunctionExpression
from statement import FunctionExpression
from expression import Expression
from expression import CallExpression
from expression import BinaryExpression
from expression import MemberExpression
from expression import Identifier
from expression import ObjectPattern
from expression import Property
from expression import Literal
from expression import AssignmentExpression
from expression import UpdateExpression
from expression import NewExpression
from expression import ObjectExpression
from expression import ConditionalExpression
from expression import UnaryExpression
from expression import ThisExpression
from expression import AssignmentPattern
from expression import AwaitExpression
from expression import LogicalExpression
from expression import ArrayExpression
from expression import TemplateLiteral
from expression import TemplateElement
from expression import SpreadElement

import json


class Program:
    def __init__(self, stmt):
        self.body = [Statement.parse(substmt) for substmt in stmt['body']]


if __name__ == '__main__':
    with open('test/ast.json', 'r') as f:
        ast = json.load(f)
    print(Program(ast))
