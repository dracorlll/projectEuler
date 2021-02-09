# Engin Yüksel
# 26.01.2021 18:46
# https://projecteuler.net/problem=3

number = 600851475143

for i in range(2, number + 1):
    if number % i == 0:
        while number % i == 0:
            number = number / i
        if number == 1:
            print("Largest Prime Number is: ", i)
            break
