import sys


n, m = map(int, sys.stdin.readline().split())
genes = []
for _ in range(n):
    genes.append(str(sys.stdin.readline().strip()))

DNA = ""

for _ in range(m):
    T, A, G, C = 0, 0, 0, 0
    for gene in genes:
        if gene[_] == "T":
            T += 1
        elif gene[_] == "A":
            A += 1
        elif gene[_] == "C":
            C += 1
        elif gene[_] == "G":
            G += 1

    if max(T, A, C, G) == A:
        DNA += "A"
    elif max(T, A, C, G) == C:
        DNA += "C"
    elif max(T, A, C, G) == G:
        DNA += "G"
    elif max(T, A, C, G) == T:
        DNA += "T"

print(DNA)

HD = 0
for _ in range(m):
    for gene in genes:
        if DNA[_] != gene[_]:
            HD += 1
print(HD)
