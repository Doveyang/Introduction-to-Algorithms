# -*- coding: utf-8 -*-
"""def MERGE(A: list, p: int, q: int, r: int) -> list:
    print(A, p, q, r)
    n1 = q - p + 1
    n2 = r - q
    L, R = list(range(n1)), list(range(n2))
    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + j + 1]
    L.append(100**100)
    R.append(100**100)
    i, j = 0, 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    return A"""


def MERGE(A: list, p: int, q: int, r: int) -> list:
    n1 = q - p + 1
    n2 = r - q
    L, R = list(range(n1)), list(range(n2))
    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + j + 1]
    for k in range(p, r + 1):
        if L[0] <= R[0]:
            A[k] = L[0]
            L.pop(0)
        else:
            A[k] = R[0]
            R.pop(0)
        if len(L) == 0 or len(R) == 0:
            for i in range(len(R)):
                A[k + i + 1] = R[i]
            for i in range(len(L)):
                A[k + i + 1] = L[i]
            break
    return A


def MERGE_SORT(A: list, p: int, r: int) -> list:
    if p < r:
        q = int((p + r) / 2)
        MERGE_SORT(A, p, q)
        MERGE_SORT(A, q + 1, r)
        MERGE(A, p, q, r)
    return A


def merge_sort(A: list) -> list:
    return MERGE_SORT(A, 0, len(A) - 1)


if __name__ == "__main__":
    print(merge_sort([31, 41, 59, 26, 41, 58]))
