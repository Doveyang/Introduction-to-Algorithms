# -*- coding: utf-8 -*-
from Bubble_Sort import *
from Insertion_Sort import *
from Merge_Sort import *
from Selection_Sort import *
import numpy as np
import time
if __name__ == "__main__":
    A = np.random.randint(10000000, size=10000).tolist()
    print("Start Sorting")

    time_start = time.time()
    bubble_sort(A)
    time_end = time.time()
    print("Bubble Sort: {} ms.".format((time_end - time_start) * 1000))

    time_start = time.time()
    selection_sort(A)
    time_end = time.time()
    print("Selection Sort: {} ms.".format((time_end - time_start) * 1000))

    time_start = time.time()
    merge_sort(A)
    time_end = time.time()
    print("Merge Sort: {} ms.".format((time_end - time_start) * 1000))

    time_start = time.time()
    insertion_sort(A)
    time_end = time.time()
    print("Insertion Sort: {} ms.".format((time_end - time_start) * 1000))

