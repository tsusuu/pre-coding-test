import sys

board = [list(map(int, sys.stdin.readline().split())) for _ in range(19)]

cases = [(0, 1), (1, 0), (1, 1), (-1, 1)]

for y in range(19):
    for x in range(19):
        selected = board[x][y]

        if selected:
            for case in cases:
                dx, dy = case
                count = 0
                mx, my = x, y

                if 18 >= mx - dx >= 0 and 18 >= my - dy >= 0:
                    if selected == board[mx - dx][my - dy]:
                        continue

                for _ in range(5):
                    mx += dx
                    my += dy

                    if mx < 0 or my < 0 or mx > 18 or my > 18:
                        break
                    temp_select = board[mx][my]

                    if selected != temp_select:
                        break
                    count += 1

                    if _ >= 4:
                        break

                if count == 4:
                    print(selected)
                    print(x + 1, y + 1)
                    exit()


print(0)
