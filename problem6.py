# Engin Yüksel
# 28.01.2021 00:17
# https://projecteuler.net/problem=6

result = 0
for i in range(1, 101):
    for j in range(i + 1, 101):
        result += i * j

print(result * 2)
