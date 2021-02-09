# Engin Yüksel
# 30.01.2021 00:34
# https://projecteuler.net/problem=15

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


print(factorial(40) / (factorial(20) * factorial(20)))
