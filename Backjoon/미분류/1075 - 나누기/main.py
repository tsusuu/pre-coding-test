import sys

getNum = int(sys.stdin.readline().strip())
getDiv = int(sys.stdin.readline().strip())


getNum = int(getNum / 100) * 100
while getNum % getDiv != 0:
    getNum += 1
print(str(getNum)[-2:])
