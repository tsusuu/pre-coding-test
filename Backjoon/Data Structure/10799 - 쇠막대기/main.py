str = input()


openBracket = 0
closeBracket = 0
result = 0
for _ in range(len(str)):
    if str[_] == "(" and str[_ + 1] == ")":
        result += openBracket
    elif str[_] == ")" and str[_ - 1] == "(":
        continue
    elif str[_] == "(":
        openBracket += 1
    elif str[_] == ")":
        openBracket -= 1
        closeBracket += 1

result += closeBracket
print(result)
