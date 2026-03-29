import sys

a = int(sys.stdin.readline().strip())
t = int(sys.stdin.readline().strip())
x = int(sys.stdin.readline().strip())

n = 1
lenth = 4
while 1:
    if t < lenth:
        break
    lenth += 4 + n
    n += 1

game = []
for i in range(n):
    game.append(0)
    game.append(1)
    game.append(0)
    game.append(1)
    game.append(0)
    for _ in range(i + 1):
        game.append(0)
    game.append(1)
    for _ in range(i + 1):
        game.append(1)

bd = 0
for _ in range(len(game)):
    if x == 0:
        if game[_] == 0:
            bd += 1
    else:
        if game[_] == 1:
            bd += 1
    if bd == t:
        print(_ % a)
        break
