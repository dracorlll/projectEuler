# Engin Yüksel
# 28.01.2021 15:34
# https://projecteuler.net/problem=2

result = 2


def fibonacci(f1, f2):
    global result
    num = f1 + f2
    if num >= 4000000:
        return num
    else:
        if num % 2 == 0:
            result += num
        return fibonacci(f2, num)


fibonacci(1, 2)
print(result)
