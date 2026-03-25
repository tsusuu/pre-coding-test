import sys

getLines = int(sys.stdin.readline())

for i in range(0, getLines, 1):
    checkBracket = 0

    getBracket = list(sys.stdin.readline().strip())

    for j in range(0, len(getBracket), 1):
        if getBracket[j] == "(":
            checkBracket += 1
        elif getBracket[j] == ")":
            checkBracket -= 1
            if checkBracket < 0:
                break

    if not checkBracket:
        print("YES")
    else:
        print("NO")
