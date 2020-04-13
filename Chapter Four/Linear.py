# -*- coding: utf-8 -*-
def find_max_subarray(A):
    l = 0
    r = 0
    s = A[0]
    t_s = 0
    t_l = 0
    for i in range(len(A)):
        t_s = max(A[i], t_s + A[i])
        if t_s > s:
            s = t_s
            r = i
            l = t_l
        if t_s == A[i]:
            t_l = i
    return l, r, s


if __name__ == "__main__":
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print(find_max_subarray(A))