# Engin Yüksel
# 30.01.2021 02:06
# https://projecteuler.net/problem=16

num = str(2 ** 1000)
result = 0
for i in range(len(num)):
    result += int(num[i])

print(result)
