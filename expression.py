class Expression:
    def __init__(self, expr):
        assert expr['type'] == self.__class__.__name__

    @staticmethod
    def parse(expr):
        from statement import ArrowFunctionExpression, FunctionExpression
        if expr is None:
            return None
        expression_list = [
            CallExpression,
            BinaryExpression,
            MemberExpression,
            Identifier,
            FunctionExpression,
            ObjectPattern,
            Property,
            Literal,
            AssignmentExpression,
            UpdateExpression,
            NewExpression,
            ObjectExpression,
            ArrowFunctionExpression,
            ConditionalExpression,
            UnaryExpression,
            ThisExpression,
            AssignmentPattern,
            AwaitExpression,
            LogicalExpression,
            ArrayExpression,
            TemplateLiteral,
            TemplateElement,
            SpreadElement,
        ]
        expression_map = {
            expr.__name__: expr for expr in expression_list
        }
        assert expr['type'] in expression_map, 'Unknown Expression: {}'.format(expr['type'])
        return expression_map[expr['type']](expr)


class Identifier(Expression):
    def __init__(self, expr):
        super(Identifier, self).__init__(expr)
        self.name = expr['name']


class Literal(Expression):
    def __init__(self, expr):
        super(Literal, self).__init__(expr)
        self.value = expr['value']


class TemplateLiteral(Expression):
    def __init__(self, expr):
        super(TemplateLiteral, self).__init__(expr)
        self.expressions = [Expression.parse(subexpr) for subexpr in expr['expressions']]
        self.quasis = [Expression.parse(subexpr) for subexpr in expr['quasis']]


class SpreadElement(Expression):
    def __init__(self, expr):
        super(SpreadElement, self).__init__(expr)
        self.argument = Expression.parse(expr['argument'])


class TemplateElement(Expression):
    def __init__(self, expr):
        super(TemplateElement, self).__init__(expr)
        self.value = expr['value']


class ObjectPattern(Expression):
    def __init__(self, expr):
        super(ObjectPattern, self).__init__(expr)
        self.properties = [Expression.parse(subexpr) for subexpr in expr['properties']]


class AssignmentPattern(Expression):
    def __init__(self, expr):
        super(AssignmentPattern, self).__init__(expr)
        self.left = Expression.parse(expr['left'])
        self.right = Expression.parse(expr['right'])


class ObjectExpression(Expression):
    def __init__(self, expr):
        super(ObjectExpression, self).__init__(expr)
        self.properties = [Expression.parse(subexpr) for subexpr in expr['properties']]


class AwaitExpression(Expression):
    def __init__(self, expr):
        super(AwaitExpression, self).__init__(expr)
        self.argument = Expression.parse(expr['argument'])


class UnaryExpression(Expression):
    def __init__(self, expr):
        super(UnaryExpression, self).__init__(expr)
        self.operator = expr['operator']
        self.argument = Expression.parse(expr['argument'])


class ThisExpression(Expression):
    def __init__(self, expr):
        super(ThisExpression, self).__init__(expr)


class LogicalExpression(Expression):
    def __init__(self, expr):
        super(LogicalExpression, self).__init__(expr)
        self.left = Expression.parse(expr['left'])
        self.operator = expr['operator']
        self.right = Expression.parse(expr['right'])


class ConditionalExpression(Expression):
    def __init__(self, expr):
        super(ConditionalExpression, self).__init__(expr)
        self.test = Expression.parse(expr['test'])
        self.consequent = Expression.parse(expr['consequent'])
        self.alternate = Expression.parse(expr['alternate'])


class ArrayExpression(Expression):
    def __init__(self, expr):
        super(ArrayExpression, self).__init__(expr)
        self.elements = [Expression.parse(subexpr) for subexpr in expr['elements']]


class Property(Expression):
    def __init__(self, expr):
        super(Property, self).__init__(expr)
        self.key = Expression.parse(expr['key'])
        self.value = Expression.parse(expr['value'])


class CallExpression(Expression):
    def __init__(self, expr):
        super(CallExpression, self).__init__(expr)
        self.callee = Expression.parse(expr['callee'])
        self.arguments = [Expression.parse(subexpr) for subexpr in expr['arguments']]


class NewExpression(Expression):
    def __init__(self, expr):
        super(NewExpression, self).__init__(expr)
        self.callee = Expression.parse(expr['callee'])
        self.arguments = [Expression.parse(subexpr) for subexpr in expr['arguments']]


class UpdateExpression(Expression):
    def __init__(self, expr):
        super(UpdateExpression, self).__init__(expr)
        self.operator = expr['operator']
        self.argument = Expression.parse(expr['argument'])


class AssignmentExpression(Expression):
    def __init__(self, expr):
        super(AssignmentExpression, self).__init__(expr)
        self.left = Expression.parse(expr['left'])
        self.operator = expr['operator']
        self.right = Expression.parse(expr['right'])


class BinaryExpression(Expression):
    def __init__(self, expr):
        super(BinaryExpression, self).__init__(expr)
        self.left = Expression.parse(expr['left'])
        self.operator = expr['operator']
        self.right = Expression.parse(expr['right'])


class MemberExpression(Expression):
    def __init__(self, expr):
        super(MemberExpression, self).__init__(expr)
        self.object = Expression.parse(expr['object'])
        self.property = Expression.parse(expr['property'])

