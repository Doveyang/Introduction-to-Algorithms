# -*- coding: utf-8 -*-
def selection_sort(li: list) -> list:
    for i in range(len(li) - 1):
        smallest = i
        for j in range(i + 1, len(li)):
            if li[j] < li[smallest]:
                smallest = j
        li[i], li[smallest] = li[smallest], li[i]
    return li


if __name__ == "__main__":
    print(selection_sort([31, 41, 59, 26, 71, 58]))
