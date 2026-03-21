import sys

n = int(sys.stdin.readline().strip())

work = []
for _ in range(n):
    T, P = map(int, sys.stdin.readline().split())
    work.append((T, P))

perIn = []
for w in work:
    (perIn.append(float(w[1] / w[0])))


total = 0
for _ in range(n):
    # maxValue = max(perIn)
    # maxIndex = [i for i, val in enumerate(perIn) if val == maxValue]
    # if len(maxIndex) == 1:
    #     maxIndex = maxIndex[0]
    # else:
    #     temp = []
    #     for i in maxIndex:
    #         temp.append((i, work[i][1]))
    #         index, tempMaxValue = max(work)
    #         maxIndex = index
    maxValue = (
        max(range(len(work)), key=lambda i: (work[i][1] / work[i][0], work[i][0])),
    )

    maxIndex = maxValue[0]

    if perIn[maxIndex] == -1:
        continue

    if n < maxIndex + work[maxIndex][0]:
        work[maxIndex] = (-1, -1)
        perIn[maxIndex] = 0
        continue
    for i in range(maxIndex + 1, maxIndex + work[maxIndex][0] - 1):
        if perIn[i] == -1:
            work[maxIndex] = (-1, -1)
            perIn[maxIndex] = 0

    usable = 1
    for i in range(maxIndex, maxIndex + work[maxIndex][0]):
        if perIn[i] == -1:
            usable = 0

    if usable:
        total += work[maxIndex][1]
        for i in range(maxIndex, maxIndex + work[maxIndex][0]):
            work[i] = (-1, -1)
            perIn[i] = -1


print(total)
