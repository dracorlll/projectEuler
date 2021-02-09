# Engin Yüksel
# 31.01.2021 18:51
# https://projecteuler.net/problem=20

result = 1
total = 0

for i in range(1, 101):
    result *= i

for i in range(len(str(result))):
    total += int(str(result)[i])

print(total)
