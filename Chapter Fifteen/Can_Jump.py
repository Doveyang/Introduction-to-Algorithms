# -*- coding: utf-8 -*-
from functools import reduce


def td_can_jump(nums: list) -> bool:
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


def bu_can_jump(nums: list) -> bool:
    ref = {0: 1}

    for k in range(1, len(nums)):
        ref[k] = False
        for i in range(k):
            if ref[i] and i + nums[i] >= k:
                ref[k] = True
                break

    return ref[len(nums) - 1]


def greedy_can_jump(nums: list) -> bool:
    pos = len(nums) - 1
    for i in reversed(range(len(nums))):
        if i + nums[i] >= pos:
            pos = i
    return pos == 0


if __name__ == "__main__":
    print(greedy_can_jump([1 for i in range(25000)]))
