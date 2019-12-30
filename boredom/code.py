from __future__ import print_function
import sys


class NumberMap:
    def __init__(self):
        self.map = []
        self.points = 0

    def push(self, x):
        if len(self.map) == 0:
            self.map.append([x, 1])

        else:
            for i in range(len(self.map)):
                if self.map[i][0] == x:
                    self.map[i][1] += 1
                    return

            self.map.append([x, 1])

    def eat(self, a_list):
        for x in a_list:
            self.push(x)

    def delete_nums(self, num_map, value):
        map_copy = num_map.copy()

        for i in range(len(map_copy)):
            num_element = map_copy[i]
            if (num_element[0] == (value - 1)) or num_element[0] == (value + 1):
                num_map.remove(num_element)
        return num_map

    def get_pts_list(self, num_map):
        pts_list = []
        for e in num_map:
            pts = e[0] * e[1]

            sub_map = num_map.copy()
            sub_map.remove(e)

            if len(sub_map) > 0:
                remain_map = self.delete_nums(sub_map, e[0])

                if len(remain_map) == 0:
                    pts_list.append(pts)
                    continue

                sub_pts_list = self.get_pts_list(remain_map)

                for i in range(len(sub_pts_list)):
                    pts_list.append((sub_pts_list[i] + pts))
            else:
                return [pts]
        return pts_list

if __name__ == "__main__":

    # 9
    # 1 2 1 3 2 2 2 2 3
    n = int(input())
    a = [int(x) for x in input().split()]

    map = NumberMap()
    map.eat(a)
    pts_list = map.get_pts_list(map.map)

    print(max(pts_list))
