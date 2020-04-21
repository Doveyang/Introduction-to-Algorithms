# -*- coding: utf-8 -*-
from functools import reduce


def can_jump(nums: list) -> bool:
    ref = {0: 1}

    def m_can_jump(k):
        if k in ref:
            return ref[k]
        path = []
        for i in range(k):
            path.append((m_can_jump(i) and i + nums[i] >= k))
        can = reduce(lambda a, b: a or b, path)
        ref[k] = can
        return can

    return m_can_jump(len(nums) - 1)


if __name__ == "__main__":
    print(can_jump([1 for i in range(25000)]))
