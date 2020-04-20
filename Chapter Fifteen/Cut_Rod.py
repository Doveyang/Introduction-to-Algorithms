# -*- coding: utf-8 -*-
import time


def cut_rod(p: list, n: int) -> float:
    if n == 0:
        return 0
    q = float("-inf")
    for i in range(1, n + 1):
        q = max(q, p[i - 1] + cut_rod(p, n - i))
    return q


def memoized_cut_rod(p: list, n: int) -> float:
    ref = {0: 0}

    def m_cut_rod(_p: list, _n: int) -> float:
        if _n in ref:
            return ref[_n]
        q = float("-inf")
        for i in range(1, _n + 1):
            q = max(q, p[i - 1] + m_cut_rod(p, _n - i))
        ref[_n] = q
        return q

    return m_cut_rod(p, n)


def bottom_up_cut_rod(p: list, n: int) -> float:
    ref = {0: 0}
    for j in range(1, n + 1):
        q = float('-inf')
        for i in range(1, j + 1):
            q = max(q, p[i - 1] + ref[j - i])
        ref[j] = q
    return ref[n]


if __name__ == "__main__":
    P = list(range(20))
    N = 20

    time_start = time.time()
    cut_rod(P, N)
    time_end = time.time()
    print("Cut Rod: {} ms.".format((time_end - time_start) * 1000))

    time_start = time.time()
    memoized_cut_rod(P, N)
    time_end = time.time()
    print("Memoized Cut Rod: {} ms.".format((time_end - time_start) * 1000))

    time_start = time.time()
    bottom_up_cut_rod(P, N)
    time_end = time.time()
    print("Bottom Up Cut Rod: {} ms.".format((time_end - time_start) * 1000))
