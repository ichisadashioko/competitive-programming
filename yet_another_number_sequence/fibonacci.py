from __future__ import print_function
import sys
import time
import numpy as np
import matplotlib.pyplot as plt


class LimitQueue:
    def __init__(self, size):
        self.size = size
        self.queue = []

    def push(self, value):
        self.queue.append(value)
        while len(self.queue) > self.size:
            self.queue.pop(0)


def optmize_fibonacci(n):
    fibs = LimitQueue(3)
    fibs.push(0)
    fibs.push(1)
    for i in range(2, n+1):
        x = fibs.queue[-1] + fibs.queue[-2]
        fibs.push(x)

    return fibs.queue[-1]


def fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibonacci(i-1) + fibonacci(i-2)


def fibonacci_to(n):
    fibs = [0, 1]
    for i in range(2, n + 1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


def fibonacci_to(n):
    fibs = [0, 1]
    for i in range(2, n + 1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


if __name__ == "__main__":
    # input = [int(x) for x in input().split()]
    # n = input[0]

    # # print(fibonacci(n))

    # s = time.time()

    # for i in range(1, (n + 1), 1):
    #     # start_time = time.time()
    #     # fibonacci(i)
    #     # fibonacci_to(i)[-1]
    #     optmize_fibonacci(i)
    #     # end_time = time.time()

    #     # print("%d takes %f" % (i, end_time-start_time))
    # e = time.time()
    # print("calculate {} fibonacci numbers takes {}s".format(n, e-s))

    fib_a = 1
    fib_b = 1

    fib_array = []

    # for i in range(10**10):

    #     fib_array.append([i, fib_b])
    #     fib_b += fib_a
    #     fib_a = fib_b - fib_a
    n = 10**6

    start = time.time()
    for i in range(1, (n + 1), 1):
        fib_b += fib_a
        fib_a = fib_b - fib_a

    end = time.time()

    print("fib({}) = {} takes {}s".format(n, fib_b, end-start))
    # x_max = np.max(fib_array[:,0])
    # y_max = np.max(fib_array[:,0])
    # fib_array = np.array(fib_array)
    # x_max = max(fib_array[:, 0])
    # y_max = max(fib_array[:, 1])

    # plt.plot(fib_array)
    # # plt.xlim([0, x_max])
    # # plt.ylim([0, y_max])
    # plt.show()
