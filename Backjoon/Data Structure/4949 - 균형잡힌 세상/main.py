import sys

getString = sys.stdin.readline().rstrip()


def isValid(getList):
    stack = []
    for i in getList:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == "(" and i == ")":
            stack.pop()
        elif stack[-1] == "[" and i == "]":
            stack.pop()
        else:
            stack.append(i)
    if len(stack) == 0:
        print("yes")
    else:
        print("no")


while getString != ".":
    bracket = []
    for i in getString:
        if i in ["(", ")", "[", "]"]:
            bracket.append(i)
    isValid(bracket)

    getString = sys.stdin.readline().rstrip()
