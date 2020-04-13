# -*- coding: utf-8 -*-
def insertion_sort(li: list) -> list:
    for j in range(1, len(li)):
        key = li[j]
        i = j - 1
        while i >= 0 and li[i] > key:
            li[i + 1] = li[i]
            i -= 1
        li[i + 1] = key
    return li


if __name__ == "__main__":
    print(insertion_sort([31, 41, 59, 26, 41, 58]))
