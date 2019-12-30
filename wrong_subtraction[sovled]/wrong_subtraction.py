import sys


def wrong_subtract(x):
    if(x % 10 == 0):
        return int(x / 10)
    else:
        return int(x - 1)

if __name__ == "__main__":
    x, n = [int(a) for a in input().split()]

    for i in range(n):
        x = wrong_subtract(x)
    
    print(x)