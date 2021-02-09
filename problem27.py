# Engin Yüksel
# 4.02.2021 06:33
# https://projecteuler.net/problem=27


def isPrime(num):
    prime = False
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
        prime = True
    if num == 2:
        prime = True
    return prime


product, maximum = 0, 0
for i in range(-999, 1000):
    for j in range(-999, 1001):
        n = 0
        counter = 0
        while True:
            if isPrime(n ** 2 + i * n + j) is not True:
                break
            counter += 1
            n += 1
        if counter > maximum:
            maximum = counter
            product = i * j

print(product)
