import sys

N = int(sys.stdin.readline())
seat = [[0] * N for _ in range(N)]

students = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N**2)]

mx = [-1, 1, 0, 0]
my = [0, 0, -1, 1]

for student in students:
    weight = []

    for x in range(N):
        for y in range(N):
            if seat[x][y] == 0:
                prefer, empty = 0, 0

                for _ in range(4):
                    dx = x + mx[_]
                    dy = y + my[_]

                    if 0 <= dx < N and 0 <= dy < N:
                        if seat[dx][dy] in student[1:]:
                            prefer += 1

                        if seat[dx][dy] == 0:
                            empty += 1

                # 가중치를 더하여 우선순위를 구하는 방법, 어떻게 작동하는지에 대해 더 자세히 공부할 필요가 있음
                weight.append((x, y, prefer, empty))

    # 람다의 사용법에 대해서 더 자세히 공부할 것
    weight.sort(key=lambda x: (-x[2], -x[3], x[0], x[1]))
    seat[weight[0][0]][weight[0][1]] = student[0]

answer = 0
score = [0, 1, 10, 100, 1000]
students.sort()

for x in range(N):
    for y in range(N):
        count = 0

        for _ in range(4):
            dx = x + mx[_]
            dy = y + my[_]

            if 0 <= dx < N and 0 <= dy < N:
                if seat[dx][dy] in students[seat[x][y] - 1]:
                    count += 1
        # print(count)
        answer += score[count]

print(answer)
