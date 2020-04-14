# -*- coding: utf-8 -*-
import random


def partition(arr, p, r):
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def randomized_partition(arr, p, r):
    i = random.randint(p, r)
    arr[r], arr[i] = arr[i], arr[r]
    return partition(arr, p, r)


def randomized_qs(arr, p, r):
    if p < r:
        q = randomized_partition(arr, p, r)
        randomized_qs(arr, p, q - 1)
        randomized_qs(arr, q + 1, r)
    return arr


def randomized_quick_sort(arr):
    return randomized_qs(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    # print(partition([13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11], 0, 11))
    print(randomized_quick_sort([13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]))
