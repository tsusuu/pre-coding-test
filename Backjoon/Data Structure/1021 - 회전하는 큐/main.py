import sys
from collections import deque

N, M = sys.stdin.readline().split(" ")
N = int(N)
M = int(M)
counter = 0

que = deque(_ for _ in range(1, N + 1))


def function1():
    que.popleft()


def function2():
    que.append(que.popleft())
    global counter
    counter += 1


def function3():
    que.appendleft(que.pop())
    global counter
    counter += 1


number = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    index = que.index(number[i])

    while number[i] != que[0]:
        if index == 0:
            break
        elif len(que) - index - 1 > index:
            function2()
        elif len(que) - index - 1 < index:
            function3()
        else:
            function2()
    function1()

print(counter)
