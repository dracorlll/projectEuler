# Engin Yüksel
# 31.01.2021 20:46
# https://projecteuler.net/problem=21


def divisor(num):
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)

    return sum(divisors)


total = 0
for i in range(1, 10000):
    num = divisor(i)
    pair = divisor(num)
    if i == pair and i != num:
        total += i

print(total)
