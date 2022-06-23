
import numpy as np
import math


def do_some_sums(n=100_000):
    sum1 = np.sum(np.sin(np.arange(n)))
    sum2 = sum(math.sin(x) for x in range(n))
    make_big_array = np.zeros(1_000_000) * 0.5
    return sum1 + sum2
