# Engin Yüksel
# 2.02.2021 20:05
# https://projecteuler.net/problem=26


def divider(divisor):
    divideList = []
    quotient = "0."
    dividend = 10
    repeating = 0
    while True:
        if dividend == 0:
            break
        if dividend in divideList:
            repeating = len(divideList) - divideList.index(dividend)
            break
        elif dividend < divisor:
            divideList.append(dividend)
            dividend *= 10
            quotient += "0"
        elif dividend >= divisor:
            divideList.append(dividend)
            quotient += str(dividend // divisor)
            remainder = dividend % divisor
            dividend = remainder * 10

    return repeating


repeating = 0
d = 0
for i in range(2, 1001):
    divide = divider(i)
    if repeating < divide:
        repeating = divide
        d = i

print(d)
