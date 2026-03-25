numOfOperands = int(input())
sentence = input()
listOperand = [0] * numOfOperands

for _ in range(numOfOperands):
    listOperand[_] = int(input())


stack = []

for _ in sentence:
    if "A" <= _ <= "Z":
        stack.append(listOperand[ord(_) - ord("A")])
    else:
        secondNum = stack.pop()
        firstNum = stack.pop()

        if _ == "+":
            stack.append(firstNum + secondNum)
        elif _ == "-":
            stack.append(firstNum - secondNum)
        elif _ == "*":
            stack.append(firstNum * secondNum)
        elif _ == "/":
            stack.append(firstNum / secondNum)

print(f"{stack[0]:.2f}")
