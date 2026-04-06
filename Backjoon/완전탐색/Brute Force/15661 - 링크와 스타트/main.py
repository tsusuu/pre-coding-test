import sys


n = int(sys.stdin.readline().strip())
ability = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


pair = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        pair[i][j] = ability[i][j] + ability[j][i]


selected = [0 for _ in range(n)]
selected[0] = 1
answer = float("inf")


def dfs(idx):
    global answer

    if idx == n:
        start = []
        link = []
        for i in range(n):
            if selected[i]:
                start.append(i)
            else:
                link.append(i)

        if not link:
            return

        start_ability = 0
        for a in range(len(start)):
            for b in range(a + 1, len(start)):
                i = start[a]
                j = start[b]
                if i < j:
                    start_ability += pair[i][j]
                else:
                    start_ability += pair[j][i]

        link_ability = 0
        for a in range(len(link)):
            for b in range(a + 1, len(link)):
                i = link[a]
                j = link[b]
                if i < j:
                    link_ability += pair[i][j]
                else:
                    link_ability += pair[j][i]

        answer = min(answer, abs(start_ability - link_ability))
        return

    selected[idx] = 1
    dfs(idx + 1)

    selected[idx] = 0
    dfs(idx + 1)


dfs(1)
print(answer)
