# Engin Yüksel
# 29.01.2021 04:23
# https://projecteuler.net/problem=12

i = 1
trinum = 1

while True:
    divisor = 0
    i += 1
    trinum += i

    for j in range(1, round(trinum ** (1/2))):
        if trinum % j == 0:
            divisor += 2
    if divisor >= 500:
        print(trinum)
        break

