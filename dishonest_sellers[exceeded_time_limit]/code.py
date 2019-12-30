from __future__ import print_function
import sys

# '''
# 3 1
# 5 4 6
# 3 1 5
# '''

if __name__ == "__main__":
    n, k = [int(x) for x in input().split()]
    discounted_items = [int(x) for x in input().split()]
    _items = [int(x) for x in input().split()]

    d = []
    for i in range(n):
        d.append(discounted_items[i] - _items[i])

    # print(*d)

    buy_list = []
    bought_count = 0

    for i in range(n):
        buy_list.append(0)

    for i in range(n):
        if d[i] < 0:
            buy_list[i] = discounted_items[i]
            bought_count += 1

    if bought_count < k:
        while bought_count < k:

            least_change_price = -1
            least_change_idx = 0

            for i in range(n):
                if buy_list[i] == 0:
                    if least_change_price < 0:
                        least_change_price = discounted_items[i]
                        least_change_idx = i
                    elif least_change_price > d[i]:
                        least_change_price = discounted_items[i]
                        least_change_idx = i

            buy_list[least_change_idx] = discounted_items[least_change_idx]
            bought_count += 1

    for i in range(n):
        if buy_list[i] == 0:
            buy_list[i] = _items[i]

    print(sum(buy_list))
