import sys

n = 19
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

cases = [(1, 0), (-1, 1), (1, 1), (0, 1)]

for y in range(n):
    for x in range(n):
        selected = board[x][y]
        if selected:
            for case in cases:
                dx, dy = case
                mx, my = x, y
                count = 0

                if 0 <= mx - dx <= 18 and 0 <= my - dy <= 18:
                    if selected == board[mx - dx][my - dy]:
                        continue

                for _ in range(5):
                    mx += dx
                    my += dy

                    if mx > n - 1 or my > n - 1:
                        break
                    elif my < 0:
                        break

                    if selected != board[mx][my]:
                        break
                    count += 1

                    if _ >= 4:
                        break

                if count == 4:
                    print(board[x][y])
                    print(x + 1, y + 1)
                    exit()
print(0)
