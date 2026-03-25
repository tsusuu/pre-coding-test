import sys

numOfEvent = int(sys.stdin.readline().strip())

for _ in range(numOfEvent):
    password = list(sys.stdin.readline().strip())
    stack = []
    temp = []
    result = ""
    for i in password:
        if i == "<":
            if len(stack):
                temp.append(stack.pop())
        elif i == ">":
            if len(temp):
                stack.append(temp.pop())
        elif i == "-":
            if len(stack):
                stack.pop()
        else:
            stack.append(i)

    stack.extend(reversed(temp))
    print("".join(stack))
