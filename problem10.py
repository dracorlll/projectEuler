# Engin Yüksel
# 28.01.2021 17:21
# https://projecteuler.net/problem=10

result = 0


def isprime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6

    return True


for j in range(2000000):
    if isprime(j):
        result += j

print(result)
