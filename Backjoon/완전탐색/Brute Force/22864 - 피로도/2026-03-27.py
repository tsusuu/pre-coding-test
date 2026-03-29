import sys

a, b, c, m = map(int, sys.stdin.readline().split())

time = 0
stress = 0
count = 0

while time < 24:
    if stress + a <= m:
        stress += a
        time += 1
        count += 1
    else:
        stress -= c
        time += 1
        if stress <= 0:
            stress = 0
print(count * b)
