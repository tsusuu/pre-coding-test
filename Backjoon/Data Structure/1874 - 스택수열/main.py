# 미완, 반례찾기
import sys
from collections import deque

n = int(sys.stdin.readline())

tempList = deque(i for i in range(1, n + 1))
stack = list()


pointer = 0

while len(tempList):
    integer = int(sys.stdin.readline())

    while not integer == tempList[pointer]:
        stack.append("+")
        pointer += 1

    if integer == tempList[pointer - 1]:
        stack.append("-")
        tempList.remove(integer)
        pointer -= 1

    elif integer < tempList[pointer - 1]:
        stack.append("NO")
        print("NO")
        break


if not stack.count("NO"):
    for i in stack:
        print(i)
