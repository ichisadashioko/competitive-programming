from __future__ import print_function
import sys
# import time


# def fibonacci(i):
#     if i == 1:
#         return 1
#     elif i == 2:
#         return 2
#     else:
#         return fibonacci(i-1) + fibonacci(i-2)


# def fibonacci_to(n):
#     fibs = [1, 1]
#     for i in range(2, n + 1):
#         fibs.append(fibs[-1] + fibs[-2])
#     return fibs


if __name__ == "__main__":
    input = [int(x) for x in input().split()]

    n = input[0]
    k = input[1]

    sum = 0

    # fibs = fibonacci_to(n)

    fib_a = 1
    fib_b = 1

    limit = 10**9

    for i in range(1, (n + 1), 1):
        # start_time = time.time()
        # Ai = fibs[i] * i**k
        # Ai = fibonacci(i) * i**k
        Ai = fib_b * (i ** k)
        sum += (Ai % limit)

        fib_b += fib_a
        fib_a = fib_b - fib_a

        # end_time = time.time()

        # print("%d takes %f" % (i, end_time-start_time))
    print(sum)
