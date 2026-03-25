import sys


def push(list, x):
    list.append(x)


def pop(list):
    if list:
        popList = list.pop()
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


def top(list):
    if not list:
        print(-1)
    else:
        print(list[-1], end="")


intList = list()

getCommandLines = int(sys.stdin.readline())
for i in range(0, getCommandLines, 1):
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
    elif "top" in getCommand:
        top(intList)
