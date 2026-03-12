import sys

A, B, C, M = map(int, sys.stdin.readline().split())

work = 0
stress = 0
time = 0

if A > M:
    print(0)
else:
    while time < 24:
        if stress < M:
            stress += A

            if stress > M:
                stress -= A
                stress -= C

                if stress <= 0:
                    stress = 0

                time += 1
                continue

            else:
                work += B
                time += 1

        else:
            stress -= C
            if stress < 0:
                stress = 0
            time += 1

    print(work)
