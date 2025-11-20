import sys


def checkArray(array, x, y):

    get = list()

    count = 0

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for x in range(len(array)):
        for y in range(len(array[x])):
            for mode in range(4):
                testX = x + dx[mode]
                testY = y + dy[mode]
                if testX < 0 or testX > len(array) or testY < 0 or testY > len(array):
                    continue
                elif array[testX][testY] == 0:
                    continue
                elif array[testX][testY] == 1:
                    test = array[testX][testY]
                    count += 1


getMatrix = int(sys.stdin.readline())

matrix = [[0 for _ in range(getMatrix)] for _ in range(getMatrix)]

for i in range(0, getMatrix, 1):
    matrix[i] = list(sys.stdin.readline().strip())


for i in range(getMatrix):
    print(matrix[i])
