# https://velog.io/@ckstn0777/%EB%B0%B1%EC%A4%80-22866%EB%B2%88-%ED%83%91-%EB%B3%B4%EA%B8%B0
import sys
from collections import deque

N = int(sys.stdin.readline().strip())
buildings = list(map(int, sys.stdin.readline().strip().split()))

stack1 = []
counter1 = []
for idx, building in enumerate(buildings):
    if not stack1:
        stack1.append([idx + 1, building])

    while stack1 and stack1[-1][1] < building:
        stack1.pop()

    if not stack1:
        stack1.append([idx + 1, building])

    elif stack1[-1][1] != building:
        stack1.append([idx + 1, building])
    counter1.append(len(stack1))

stack2 = []
counter2 = []
temp = reversed(buildings)
for idx, building in enumerate(temp):
    if not stack2:
        stack2.append([idx + 1, building])

    while stack2 and stack2[-1][1] < building:
        stack2.pop()

    if not stack2:
        stack2.append([idx + 1, building])

    elif stack2[-1][1] != building:
        stack2.append([idx + 1, building])
    counter2.append(len(stack2))

for _ in range(len(counter1)):
    counter1[_] = counter1[_] + counter2[-(_ + 1)] - 2
