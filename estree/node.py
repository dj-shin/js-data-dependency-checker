class Node:
    def __init__(self, loc=None):
        self.loc = loc


class SourceLocation:
    def __init__(self, source, start, end):
        self.source = source
        self.start = start
        self.end = end


class Position:
    def __init__(self, line, column):
        self.line = line
        self.column = column
