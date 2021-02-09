# Engin Yüksel
# 28.01.2021 00:37
# https://projecteuler.net/problem=7

i = 1
counter = 2
isPrime = False

while True:
    i += 1
    for j in range(2, i - 1):
        if i % j == 0:
            isPrime = False
            break
        isPrime = True

    if isPrime:
        counter += 1

    if counter == 10001:
        print("10001. Prime is: ", i)
        break
