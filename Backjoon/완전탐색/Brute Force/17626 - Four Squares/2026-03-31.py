import sys
from itertools import product

n = int(sys.stdin.readline().strip())


def squares(n):
    root = n**0.5
    if root == int(root):
        return 1

    for i in range(1, int(root) + 1):
        root1 = (n - i**2) ** 0.5

        if root1 == int(root1):
            return 2

    for i in range(1, int(root) + 1):
        root2 = (n - i**2) ** 0.5

        for j in range(1, int(root2) + 1):
            root3 = (n - i**2 - j**2) ** 0.5

            if root3 == int(root3):
                return 3

    return 4


print(squares(n))
