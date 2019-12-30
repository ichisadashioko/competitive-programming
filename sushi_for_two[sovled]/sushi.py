from __future__ import print_function
import sys


class SushiCount:
    def __init__(self):
        self.eel = 0
        self.tuna = 0
        self.TUNA_VALUE = 1
        self.EEL_VALUE = 2
        self.eel_turn = False
        self.max_order = 0

    def eat(self, sushi):
        if (self.eel == 0) and (self.tuna == 0):
            if sushi == self.EEL_VALUE:
                self.eel_turn = True
                self.eel += 1
            else:
                self.eel_turn = False
                self.tuna += 1
        elif self.eel_turn:
            if sushi == self.EEL_VALUE:
                self.eel += 1
            else:
                if self.tuna == 0:
                    self.eel_turn = False
                    self.tuna += 1
                else:
                    self.check_out()
                    self.tuna = 0
                    self.eel_turn = False
                    self.eat(sushi)
        else:
            if sushi == self.TUNA_VALUE:
                self.tuna += 1
            else:
                if self.eel == 0:
                    self.eel_turn = True
                    self.eel += 1
                else:
                    self.check_out()
                    self.eel = 0
                    self.eel_turn = True
                    self.eat(sushi)

    def check_out(self):
        order_count = min(self.eel, self.tuna)
        if order_count > self.max_order:
            self.max_order = order_count


if __name__ == "__main__":
    n = int(input())
    sushi_arr = [int(x) for x in input().split()]

    # n = 9
    # sushi_arr = [2, 2, 1, 1, 1, 2, 2, 2, 2]

    sushi_counter = SushiCount()

    for i in range(n):
        sushi_counter.eat(sushi_arr[i])

    sushi_counter.check_out()

    print(sushi_counter.max_order * 2)

    pass
