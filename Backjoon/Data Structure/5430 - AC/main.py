import sys
from collections import deque


times = int(sys.stdin.readline().strip())


def R(arr):
    arr.reverse()


def Dl(arr):
    arr.popleft()


def Dr(arr):
    arr.pop()


for _ in range(times):
    function = list(sys.stdin.readline().strip())
    lenArr = int(sys.stdin.readline().strip())
    reverse = False
    arr = deque(eval(sys.stdin.readline().strip()))

    try:
        for i in function:
            if i == "R":
                reverse = not reverse
            elif i == "D":
                if reverse:
                    Dr(arr)
                else:
                    Dl(arr)

        if reverse:
            print("[" + ",".join(map(str, reversed(arr))) + "]")
        else:
            print("[" + ",".join(map(str, arr)) + "]")

    except:
        print("error")
