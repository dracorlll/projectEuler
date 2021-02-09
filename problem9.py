# Engin Yüksel
# 28.01.2021 04:16
# https://projecteuler.net/problem=9


i = 0
state = False
while not state:
    i += 1
    for j in range(i, 1000):
        sum = i ** 2 + j ** 2
        sqrt = sum ** (1 / 2)
        if sqrt.is_integer():
            if i + j + sqrt == 1000:
                print(i*j*sqrt)
                state = True
                break
