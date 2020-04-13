# -*- coding: utf-8 -*-
class heap(list):
    def __init__(self, arr):
        self.size = len(arr)
        list.__init__(self, arr)


def parent(i):
    return i // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def max_heapify(arr, i):
    l = left(i)
    r = right(i)
    if l <= arr.size - 1 and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    if r <= arr.size - 1 and arr[r] > arr[largest]:
        largest = r
    if i != largest:
        arr[largest], arr[i] = arr[i], arr[largest]
        max_heapify(arr, largest)
    return arr


def build_max_heap(arr):
    for i in reversed(range(arr.size // 2)):
        arr = max_heapify(arr, i)
    return arr


def heap_sort(arr):
    arr = heap(arr)
    arr = build_max_heap(arr)
    for i in reversed(range(1, len(arr))):
        arr[0], arr[i] = arr[i], arr[0]
        arr.size -= 1
        arr = max_heapify(arr, 0)
    return arr


if __name__ == "__main__":
    # A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    A = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
    print(heap_sort(A))
