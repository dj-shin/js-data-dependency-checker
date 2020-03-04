from expression import Expression


class Statement:
    def __init__(self, stmt):
        assert stmt['type'] == self.__class__.__name__

    @staticmethod
    def parse(stmt):
        if stmt is None:
            return None
        statement_list = [
            VariableDeclaration,
            VariableDeclarator,
            FunctionDeclaration,
            ClassDeclaration,
            ClassBody,
            BlockStatement,
            MethodDefinition,
            ReturnStatement,
            ExpressionStatement,
            IfStatement,
            BreakStatement,
            ContinueStatement,
            SwitchStatement,
            SwitchCase,
            TryStatement,
            ForStatement,
            WhileStatement,
            ForOfStatement,
            ForInStatement,
            CatchClause,
            EmptyStatement,
            LabeledStatement,
        ]
        statement_map = {
            stmt.__name__: stmt for stmt in statement_list
        }
        if stmt['type'] not in statement_map:
            return Expression.parse(stmt)
        assert stmt['type'] in statement_map, 'Unknown Statement: {}'.format(stmt['type'])
        return statement_map[stmt['type']](stmt)


class EmptyStatement(Statement):
    def __init__(self, stmt):
        super(EmptyStatement, self).__init__(stmt)


class LabeledStatement(Statement):
    def __init__(self, stmt):
        super(LabeledStatement, self).__init__(stmt)
        self.body = Statement.parse(stmt['body'])
        self.label = Expression.parse(stmt['label'])


class ExpressionStatement(Statement):
    def __init__(self, stmt):
        super(ExpressionStatement, self).__init__(stmt)
        self.expr = Expression.parse(stmt['expression'])


class CatchClause(Statement):
    def __init__(self, stmt):
        super(CatchClause, self).__init__(stmt)
        self.param = Expression.parse(stmt['param'])
        self.body = Statement.parse(stmt['body'])


class IfStatement(Statement):
    def __init__(self, stmt):
        super(IfStatement, self).__init__(stmt)
        self.test = Expression.parse(stmt['test'])
        self.consequent = Statement.parse(stmt['consequent'])
        self.alternate = Statement.parse(stmt['alternate'])


class TryStatement(Statement):
    def __init__(self, stmt):
        super(TryStatement, self).__init__(stmt)
        self.block = Statement.parse(stmt['block'])
        self.handler = Statement.parse(stmt['handler'])
        self.finalizer = Statement.parse(stmt['finalizer'])


class BlockStatement(Statement):
    def __init__(self, stmt):
        super(BlockStatement, self).__init__(stmt)
        self.body = [Statement.parse(substmt) for substmt in stmt['body']]


class SwitchCase(Statement):
    def __init__(self, stmt):
        super(SwitchCase, self).__init__(stmt)
        self.consequent = [Statement.parse(substmt) for substmt in stmt['consequent']]
        self.test = Expression.parse(stmt['test'])


class ReturnStatement(Statement):
    def __init__(self, stmt):
        super(ReturnStatement, self).__init__(stmt)
        self.argument = Expression.parse(stmt['argument'])


class BreakStatement(Statement):
    def __init__(self, stmt):
        super(BreakStatement, self).__init__(stmt)
        self.label = Expression.parse(stmt['label'])


class ContinueStatement(Statement):
    def __init__(self, stmt):
        super(ContinueStatement, self).__init__(stmt)


class ForStatement(Statement):
    def __init__(self, stmt):
        super(ForStatement, self).__init__(stmt)
        self.init = Statement.parse(stmt['init'])
        self.test = Expression.parse(stmt['test'])
        self.update = Expression.parse(stmt['update'])
        self.body = Statement.parse(stmt['body'])


class WhileStatement(Statement):
    def __init__(self, stmt):
        super(WhileStatement, self).__init__(stmt)
        self.test = Expression.parse(stmt['test'])
        self.body = Statement.parse(stmt['body'])


class ForOfStatement(Statement):
    def __init__(self, stmt):
        super(ForOfStatement, self).__init__(stmt)
        self.left = Statement.parse(stmt['left'])
        self.right = Expression.parse(stmt['right'])
        self.body = Statement.parse(stmt['body'])


class ForInStatement(Statement):
    def __init__(self, stmt):
        super(ForInStatement, self).__init__(stmt)
        self.left = Statement.parse(stmt['left'])
        self.right = Expression.parse(stmt['right'])
        self.body = Statement.parse(stmt['body'])


class SwitchStatement(Statement):
    def __init__(self, stmt):
        super(SwitchStatement, self).__init__(stmt)
        self.discriminant = Expression.parse(stmt['discriminant'])
        self.cases = [Statement.parse(substmt) for substmt in stmt['cases']]


class ClassDeclaration(Statement):
    def __init__(self, stmt):
        super(ClassDeclaration, self).__init__(stmt)
        self.id = Expression.parse(stmt['id'])
        self.body = Statement.parse(stmt['body'])


class ClassBody(Statement):
    def __init__(self, stmt):
        super(ClassBody, self).__init__(stmt)
        self.body = [Statement.parse(substmt) for substmt in stmt['body']]


class FunctionDeclaration(Statement):
    def __init__(self, stmt):
        super(FunctionDeclaration, self).__init__(stmt)
        self.id = Expression.parse(stmt['id'])
        self.params = [Expression.parse(subexpr) for subexpr in stmt['params']]
        self.body = Statement.parse(stmt['body'])


class VariableDeclaration(Statement):
    def __init__(self, stmt):
        super(VariableDeclaration, self).__init__(stmt)
        self.declarations = [Statement.parse(substmt) for substmt in stmt['declarations']]


class VariableDeclarator(Statement):
    def __init__(self, stmt):
        super(VariableDeclarator, self).__init__(stmt)
        self.id = Expression.parse(stmt['id'])
        self.init = Expression.parse(stmt['init'])


class MethodDefinition(Statement):
    def __init__(self, stmt):
        super(MethodDefinition, self).__init__(stmt)
        self.kind = stmt['kind']
        self.key = Expression.parse(stmt['key'])
        self.value = Expression.parse(stmt['value'])


class ArrowFunctionExpression(Expression):
    def __init__(self, expr):
        super(ArrowFunctionExpression, self).__init__(expr)
        self.params = [Expression.parse(subexpr) for subexpr in expr['params']]
        self.body = Statement.parse(expr['body'])


class FunctionExpression(Expression):
    def __init__(self, expr):
        super(FunctionExpression, self).__init__(expr)
        self.params = [Expression.parse(subexpr) for subexpr in expr['params']]
        self.body = Statement.parse(expr['body'])
