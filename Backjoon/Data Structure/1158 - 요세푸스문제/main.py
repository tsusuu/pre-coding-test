# 미완, 반례찾기
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().strip().split(" "))

tempList = deque(range(1, N + 1, 1))
Josephus = deque()


temp = K - 1
for i in range(N):
    Josephus.append(tempList[temp])
    tempList[temp] = 0

    for _ in range(K):
        temp += 1

        if temp >= len(tempList):
            temp = 0
        while not tempList[temp]:
            temp += 1
            if temp >= len(tempList):
                temp = 0


print("<", end="")
for i in range(0, N - 1, 1):
    print(Josephus[i], end=", ")
print(Josephus[N - 1], end=">")
