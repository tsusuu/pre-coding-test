import sys

n, m = sys.stdin.readline().strip().split(" ")
n = int(n)
m = int(m)

sum = n - m

if sum < 0:
    sum = -sum

print(sum)
