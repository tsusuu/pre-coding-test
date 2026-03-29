import sys

n, m = map(int, sys.stdin.readline().split())
genes = [sys.stdin.readline().strip() for _ in range(n)]

dist = 0
result = str()
for i in range(m):
    A, C, G, T = 0, 0, 0, 0
    for gene in genes:
        if gene[i] == "A":
            A += 1
        elif gene[i] == "C":
            C += 1
        elif gene[i] == "G":
            G += 1
        elif gene[i] == "T":
            T += 1

    if max(A, C, G, T) == A:
        result += "A"
        dist += n - A
    elif max(A, C, G, T) == C:
        result += "C"
        dist += n - C
    elif max(A, C, G, T) == G:
        result += "G"
        dist += n - G
    elif max(A, C, G, T) == T:
        result += "T"
        dist += n - T

print(result)
print(dist)
