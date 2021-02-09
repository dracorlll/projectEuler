# Engin Yüksel
# 29.01.2021 18:33
# https://projecteuler.net/problem=14

counter = 0
num = 1
for i in range(1, 1000000):
    chain = 0
    start = i
    while True:
        if i == 1:
            if chain > counter:
                counter = chain
                num = start
            break
        if i % 2 == 0:
            i = i / 2
        else:
            i = i * 3 + 1
        chain += 1

print(num)
