# -*- coding: utf-8 -*-
class StackUnderflow(ValueError):  # 栈下溢(空栈访问)，overflow暂时不考虑。
    pass


class Stack:
    def __init__(self):
        self._elements = []

    def is_empty(self):
        return self._elements == []

    def push(self, element):
        self._elements.append(element)

    def pop(self):
        if self.is_empty():
            raise StackUnderflow("in Stack.pop()")
        return self._elements.pop()

    def top(self):
        if self.is_empty():
            raise StackUnderflow("in Stack.top()")
        return self._elements[-1]


if __name__ == "__main__":
    s = Stack()
    s.push(5)
    print(s.top())
