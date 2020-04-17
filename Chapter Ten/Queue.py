# -*- coding: utf-8 -*-
class Queue(object):
    def __init__(self, n):
        self._elements = [None for _ in range(n)]
        self._tail = 0
        self._head = 0

    def enqueue(self, x):
        self._elements[self._tail] = x
        if self._tail == self._elements.__len__() - 1:
            self._tail = 0
        else:
            self._tail += 1
        return True

    def dequeue(self):
        x = self._elements[self._head]
        if self._head == self._elements.__len__() - 1:
            self._head = 0
        else:
            self._head += 1
        return x

    def empty(self):
        if self._head == self._tail:
            return True
        return False


if __name__ == "__main__":
    '''q = Queue(3)
    q.enqueue("5")
    q.enqueue("6")
    q.enqueue("9")
    # print(q.full())
    print(q.dequeue())
    q.enqueue("7")
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.empty())'''

    import queue

    q = queue.Queue(3)
    q.put("5")
    q.put("6")
    q.put("9")
    print(q.full())
    print(q.get())
    q.put("7")
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.empty())
