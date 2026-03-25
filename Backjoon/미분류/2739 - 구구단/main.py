import sys

getNum = int(sys.stdin.readline().strip())

for i in range(1, 10, 1):
    print(getNum, "*", i, "=", getNum * i)
