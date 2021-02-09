# Engin Yüksel
# 27.01.2021 22:04
# https://projecteuler.net/problem=5

import numpy as np

arr = []
for i in range(1, 21):
    arr.append(i)

print(np.lcm.reduce(arr))


# Second Method

arr = []
for i in range(1, 11):
    arr.append(i)

print(arr)
for i in range(10, 0, -1):
    for j in range(i - 1, 0, -1):
        if i % j == 0:
            if j in arr:
                arr.remove(j)

result = 1
print(arr)
for i in arr:
    result = i * result
print(result)


