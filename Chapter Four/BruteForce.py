# -*- coding: utf-8 -*-
def find_max_subarray(A):
    s = -100 ** 100
    l = 0
    r = len(A) - 1
    for i in range(len(A)):
        for j in range(i, len(A)):
            if sum(A[i:j + 1]) > s:
                s = sum(A[i:j + 1])
                l = i
                r = j
    return l, r, s


if __name__ == "__main__":
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print(find_max_subarray(A))
