from functools import reduce


class MyError(Exception):
    message: str = 'Error text'

    def __str__(self):
        return self.message


class Parent:

    def __init__(self, num=None):
        self.i = num if num is not None else 3

    def fnc(self, *args: tuple):
        if len(args) == 1 and (args[0] % 2 != 0):
            raise MyError
        if len(args) == 1:
            args = args + (args[0],)
        return reduce(lambda a, b: a * b, args, self.i)


class First:
    isSecond = 0

    def isFirst(self):
        return 1


class Second:
    isSecond = 1

    def isFirst(self):
        return 0


class A(First, Parent):
    pass
