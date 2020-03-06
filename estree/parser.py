from estree.classes import MethodDefinition, ClassBody, Class, ClassDeclaration, ClassExpression, MetaProperty
from estree.declarations import FunctionDeclaration, VariableDeclaration, VariableDeclarator, Declaration
from estree.exports import ExportSpecifier, ExportNamedDeclaration, AnonymousDefaultExportedFunctionDeclaration, \
    AnonymousDefaultExportedClassDeclaration, ExportDefaultDeclaration, ExportAllDeclaration
from estree.expression import MemberExpression, AssignmentExpression, Expression, Super, ThisExpression, SpreadElement, \
    ArrayExpression, Property, AssignmentProperty, ObjectExpression, FunctionExpression, UnaryExpression, \
    UpdateExpression, BinaryExpression, LogicalExpression, ConditionalExpression, CallExpression, NewExpression, \
    SequenceExpression, ArrowFunctionExpression, YieldExpression, AwaitExpression
from estree.functions import Function
from estree.identifier import Identifier
from estree.imports import ImportSpecifier, ImportDefaultSpecifier, ImportNamespaceSpecifier, ImportDeclaration
from estree.literal import Literal, RegExpLiteral, TemplateElement, TemplateLiteral
from estree.modules import ModuleDeclaration, ModuleSpecifier
from estree.patterns import Pattern, AssignmentPattern, ObjectPattern, ArrayPattern, RestElement
from estree.statement import Statement, FunctionBody, BlockStatement, ExpressionStatement, Directive, EmptyStatement, \
    DebuggerStatement, WithStatement, ReturnStatement, LabeledStatement, BreakStatement, ContinueStatement, \
    IfStatement, SwitchCase, SwitchStatement, ThrowStatement, CatchClause, TryStatement, WhileStatement, \
    DoWhileStatement, ForStatement, ForOfStatement, ForInStatement
from estree.program import Program


NODE_TYPES = [
    Program,
    FunctionBody,
    Identifier,
    ModuleDeclaration,
    MethodDefinition,
    ClassBody,
    Class,
    ClassDeclaration,
    ClassExpression,
    MetaProperty,
    Declaration,
    FunctionDeclaration,
    VariableDeclarator,
    VariableDeclaration,
    ExportSpecifier,
    ExportNamedDeclaration,
    AnonymousDefaultExportedFunctionDeclaration,
    AnonymousDefaultExportedClassDeclaration,
    ExportDefaultDeclaration,
    ExportAllDeclaration,
    Expression,
    Super,
    ThisExpression,
    SpreadElement,
    ArrayExpression,
    Property,
    AssignmentProperty,
    ObjectExpression,
    FunctionExpression,
    UnaryExpression,
    UpdateExpression,
    BinaryExpression,
    AssignmentExpression,
    LogicalExpression,
    MemberExpression,
    ConditionalExpression,
    CallExpression,
    NewExpression,
    SequenceExpression,
    ArrowFunctionExpression,
    YieldExpression,
    Function,
    ImportSpecifier,
    ImportDefaultSpecifier,
    ImportNamespaceSpecifier,
    ImportDeclaration,
    Literal,
    RegExpLiteral,
    TemplateElement,
    TemplateLiteral,
    ModuleSpecifier,
    Pattern,
    ObjectPattern,
    ArrayPattern,
    RestElement,
    AssignmentPattern,
    Statement,
    ExpressionStatement,
    Directive,
    BlockStatement,
    EmptyStatement,
    DebuggerStatement,
    WithStatement,
    ReturnStatement,
    LabeledStatement,
    BreakStatement,
    ContinueStatement,
    IfStatement,
    SwitchCase,
    SwitchStatement,
    ThrowStatement,
    CatchClause,
    TryStatement,
    WhileStatement,
    DoWhileStatement,
    ForStatement,
    AwaitExpression,
    ForOfStatement,
    ForInStatement,
]
NODE_MAP = {node.__name__: node for node in NODE_TYPES}


def parse(data):
    if data is None:
        return None
    elif isinstance(data, (str, int, float, bool)):
        return data
    elif isinstance(data, list):
        return [parse(item) for item in data]

    if data.get('type') is None:
        # print('Possibly invalid object {}'.format(data))
        return data
    cls = NODE_MAP.get(data['type'])
    if cls is None:
        raise Exception('Unknown type {}'.format(data['type']))
    exclude_keys = ['type', 'loc', 'start', 'end', 'raw']

    def rename_rule(key: str):
        key = key.lower()
        if key in ['object', 'property', 'id', 'async', 'await']:
            return key + '_'
        else:
            return key

    kwargs = {
        rename_rule(key): parse(data[key]) for key in data if key not in exclude_keys
    }
    try:
        return cls(**kwargs)
    except TypeError as exc:
        print(cls)
        print(kwargs)
        raise exc
