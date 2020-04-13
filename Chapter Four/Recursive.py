# -*- coding: utf-8 -*-
def FIND_MAX_XING_SUBARRAY(A, low, mid, high):
    left_sum = float("-inf")
    max_left = low
    for i in range(low, mid + 1):
        s = sum(A[i:mid + 1])
        if s > left_sum:
            left_sum = s
            max_left = i

    right_sum = float("-inf")
    max_right = high
    for i in range(mid + 1, high + 1):
        s = sum(A[mid + 1:i + 1])
        if s > right_sum:
            right_sum = s
            max_right = i
    return max_left, max_right, left_sum + right_sum


def FIND_MAX_SUBARRAY(A, low, high):
    if high == low:
        return low, high, A[low]
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = FIND_MAX_SUBARRAY(A, low, mid)
        right_low, right_high, right_sum = FIND_MAX_SUBARRAY(A, mid + 1, high)
        cross_low, cross_high, cross_sum = FIND_MAX_XING_SUBARRAY(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


def find_max_subarray(A):
    return FIND_MAX_SUBARRAY(A, 0, len(A) - 1)


if __name__ == "__main__":
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    # print(FIND_MAX_XING_SUBARRAY([-4, -5, 18, 20, -7, 12, -5], 0, 3, 6))
    print(find_max_subarray(A))
