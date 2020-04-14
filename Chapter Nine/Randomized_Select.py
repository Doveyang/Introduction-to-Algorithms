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


def randomized_select(arr, p, r, i):
    if p == r:
        return arr[p]
    q = randomized_partition(arr, p, r)
    # q = partition(arr, p, r)
    k = q - p + 1
    if i == k:
        return arr[q]
    elif i < k:
        return randomized_select(arr, p, q - 1, i)
    else:
        return randomized_select(arr, q + 1, r, i - k)


def find_median(arr):
    if len(arr) % 2 != 0:
        mid = randomized_select(arr, 0, len(arr) - 1, len(arr) // 2)
        return mid
    else:
        l = randomized_select(arr, 0, len(arr) - 1, len(arr) // 2)
        r = randomized_select(arr, 0, len(arr) - 1, len(arr) // 2 + 1)
        mid = (l + r) / 2
        return mid


if __name__ == "__main__":
    print(find_median([13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]))
