import sys

H, W = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline().strip())

sticker = []
for _ in range(N):
    R, C = map(int, sys.stdin.readline().split())
    sticker.append((R, C))

extend = 0

for i in range(N):
    for j in range(i + 1, N):
        r1, c1 = sticker[i]
        r2, c2 = sticker[j]

        cases = [(r1, c1, r2, c2), (c1, r1, r2, c2), (r1, c1, c2, r2), (c1, r1, c2, r2)]

        for r1, c1, r2, c2 in cases:
            if (
                (r1 + r2) <= H
                and max(c1, c2) <= W
                or (r1 + r2) <= W
                and max(c1, c2) <= H
            ):
                extend = max(extend, r1 * c1 + r2 * c2)
                break

            if (
                (c1 + c2) <= H
                and max(r1, r2) <= W
                or (c1 + c2) <= H
                and max(r1, r2) <= W
            ):
                extend = max(extend, r1 * c1 + r2 * c2)
                break
print(extend)
