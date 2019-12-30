from __future__ import print_function
import sys


def fibonacci_to(n):
    fibs = [0, 1]
    for i in range(2, n + 1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

if __name__ == "__main__":
    input = [int(x) for x in input().split()]

    n = input[0]

    print(fibonacci(n))
