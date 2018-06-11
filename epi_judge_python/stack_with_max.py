from test_framework import generic_test
from test_framework.test_failure import TestFailure
import sys

class Stack:
    def __init__(self):
        self.data = []
        self.max_cached = []

    def empty(self):
        # TODO - you fill in here.
        return len(self.data) == 0

    def max(self):
        # TODO - you fill in here.
        val = None
        if self.max_cached:
            val, _ = self.max_cached[-1]
        return val

    def pop(self):
        # TODO - you fill in here.
        if self.empty():
            x = None
        else:
            x = self.data.pop()
            val, count = self.max_cached[-1]
            if x == val:
                count -= 1
                if count == 0:
                    self.max_cached.pop()
                else:
                    self.max_cached[-1] = [val, count]
        return x

    def push(self, x):
        # TODO - you fill in here.
        val, count = -sys.maxsize, 0
        self.data.append(x)
        if self.max_cached:
            val, count = self.max_cached[-1]
        if x > val:
            self.max_cached.append([x, 1])
        elif x == val:
            self.max_cached[-1] = [x, count+1]


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure(
                        "Pop: expected " + str(arg) + ", got " + str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure(
                        "Empty: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported stack operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("stack_with_max.py",
                                       'stack_with_max.tsv', stack_tester))
