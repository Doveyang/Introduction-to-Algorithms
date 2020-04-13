import Linear
import BruteForce
import Recursive
import numpy as np
import time
if __name__ == "__main__":
    A = np.random.randint(-100, 100, 1000).tolist()
    t0 = time.time()
    Linear.find_max_subarray(A)
    print("Linear: {} ms.".format((time.time()-t0)*1000))

    t0 = time.time()
    Recursive.find_max_subarray(A)
    print("Recursive: {} ms.".format((time.time()-t0)*1000))

    t0 = time.time()
    BruteForce.find_max_subarray(A)
    print("BruteForce: {} ms.".format((time.time() - t0) * 1000))

    t0 = time.time()
    BruteForce.find_max_subarray(A)
    print("BruteForce: {} ms.".format((time.time() - t0) * 1000))
