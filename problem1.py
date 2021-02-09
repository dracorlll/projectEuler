# Engin Yüksel
# 28.01.2021 15:30
# https://projecteuler.net/problem=1

result = 0
for i in range(10):
    if i % 3 == 0 or i % 5 == 0:
        result += i

print(result)
