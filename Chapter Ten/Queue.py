# -*- coding: utf-8 -*-
class Queue(object):
    def __init__(self, n):
        self._elements = [None for _ in range(n)]
        self._tail = 0
        self._head = 0

    def enqueue(self, x):
        self._elements[self._tail] = x
        if self._tail == self._elements.__len__():
            self._tail = 0
        else:
            self._tail += 1
        return True

    def dequeue(self):
        x = self._elements[self._head]
        if self._head == self._elements.__len__():
            self._head = 0
        else:
            self._head += 1
        return x


if __name__ == "__main__":
    q = Queue(3)
    q.enqueue("5")
    q.enqueue("6")
    print(q.dequeue())
    q.enqueue("7")
    print(q.dequeue())
    print(q.dequeue())
