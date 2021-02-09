# Engin Yüksel
# 1.02.2021 20:37
# https://projecteuler.net/problem=25


f1 = 1
f2 = 2

i = 3
while True:
    i += 1
    f3 = f1 + f2
    if len(str(f3)) == 1000:
        print(i)
        break
    f1 = f2
    f2 = f3
