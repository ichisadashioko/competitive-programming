from __future__ import print_function
import sys

if __name__ == "__main__":
    n, k = [int(x) for x in input().split()]

    sum = 0

    fib_a = 1
    fib_b = 1

    limit = 10**9

    for i in range(1, (n + 1), 1):
        Ai = fib_b * (i ** k)
        sum += (Ai % limit)

        fib_b += fib_a
        fib_a = fib_b - fib_a
    print(sum)
