# Engin Yüksel
# 4.02.2021 07:53
# https://projecteuler.net/problem=28

result = 0
for i in range(2, 1002, 2):
    result += 4 * (i ** 2) + 2 * i + 4
print(result + 1)
