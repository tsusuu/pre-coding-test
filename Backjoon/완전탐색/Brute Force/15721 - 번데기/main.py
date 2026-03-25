import sys

A = int(sys.stdin.readline())
T = int(sys.stdin.readline())
x = int(sys.stdin.readline())

temp = list()
n = 0

calclenth = T
while calclenth > 0:
    calclenth -= 4 + n
    n += 1

times = 2
for _ in range(n):
    temp.append(0)
    temp.append(1)
    temp.append(0)
    temp.append(1)
    for _ in range(times):
        temp.append(0)
    for _ in range(times):
        temp.append(1)
    times += 1
bbun = 0
degi = 0

for _ in range(len(temp)):
    if x == 0:
        if temp[_] == 0:
            bbun += 1
        if bbun == T:
            print(_ % A)
            break
    else:
        if temp[_] == 1:
            degi += 1
        if degi == T:
            print(_ % A)
            break
