# -*- coding: utf-8 -*-
def bubble_sort(A: list) -> list:
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A))[::-1]:
            if A[j] < A[j -1]:
                A[j], A[j - 1] = A[j - 1], A[j]
    return A


if __name__ == "__main__":
    print(bubble_sort([31, 41, 59, 26, 41, 58]))
