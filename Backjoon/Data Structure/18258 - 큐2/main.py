import sys
from collections import deque


def push(list, x):
    list.append(x)


def pop(list):
    if list:
        popList = list.popleft()
        print(popList, end="")
    else:
        print(-1)


def size(list):
    print(len(list))


def empty(list):
    if not list:
        print(1)
    else:
        print(0)


def front(list):
    if not list:
        print(-1)
    else:
        print(list[0], end="")


def back(list):
    if not list:
        print(-1)
    else:
        print(list[-1], end="")


intList = deque([])

getCommandLines = int(sys.stdin.readline())
for _ in range(0, getCommandLines, 1):
    getCommand = sys.stdin.readline()

    if "push" in getCommand:
        getCommand, getNum = getCommand.split(" ")
        push(intList, getNum)
    elif "pop" in getCommand:
        pop(intList)
    elif "size" in getCommand:
        size(intList)
    elif "empty" in getCommand:
        empty(intList)
    elif "front" in getCommand:
        front(intList)
    elif "back" in getCommand:
        back(intList)
