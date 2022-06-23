
import numpy as np
import time


def slow_function_1(x):
    time.sleep(3)
    return x


def frequently_called_function(x):
    time.sleep(0.001)
    return x


def slow_function_2(x):
    time.sleep(1)
    result = slow_function_1(x)
    for ii in range(10_000):
        result += frequently_called_function(x)
    return result


if __name__ == "__main__":

    print(slow_function_2(1))
