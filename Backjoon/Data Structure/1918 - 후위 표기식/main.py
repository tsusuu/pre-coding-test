import sys

expression = sys.stdin.readline().strip()
result = ""
stack = []
priority = {"*": 1, "/": 1, "+": -1, "-": -1}


for i in "(" + expression + ")":
    if i.isalpha():
        result += i
    elif i == ")":
        temp = stack.pop()
        while temp != "(":
            result += temp
            temp = stack.pop()
    else:
        if i != "(":
            while stack[-1] != "(" and priority[i] <= priority[stack[-1]]:
                result += stack.pop()
        stack.append(i)
print(result)
