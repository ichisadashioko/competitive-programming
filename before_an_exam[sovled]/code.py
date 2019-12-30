from __future__ import print_function
import sys

if __name__ == "__main__":
    d, sum_time = [int(x) for x in input().split()]

    min_arr = []
    max_arr = []

    for i in range(d):
        min_time, max_time = [int(x) for x in input().split()]
        min_arr.append(min_time)
        max_arr.append(max_time)

    if sum_time >= sum(min_arr) and sum_time <= sum(max_arr):
        print("YES")

        schedule = []

        for i in range(d):
            schedule.append(min_arr[i])
            sum_time -= min_arr[i]

        while sum_time > 0:
            for i in range(d):
                if not (sum_time > 0):
                    break

                if schedule[i] < max_arr[i]:
                    schedule[i] += 1
                    sum_time -= 1

        print(*schedule)

    else:
        print("NO")
