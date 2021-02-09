# Engin Yüksel
# 27.01.2021 20:27
# https://projecteuler.net/problem=4

max = 999
min = 99
palindromes = 0

for i in range(max, min, -1):
    for j in range(max, min, -1):
        number = i * j
        if str(number) == str(number)[::-1]:
            if number > palindromes:
                palindromes = number
                break

print("Largest palindrome product is: ", palindromes)
