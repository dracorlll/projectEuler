# Engin Yüksel
# 4.02.2021 10:36
# https://projecteuler.net/problem=30


index = 1
res = 0
while True:
    index += 1
    num = 0
    for i in range(len(str(index))):
        num += int(str(index)[i]) ** 5
    if num == index:
        res += index
    if index == 5 * 9 ** 5:
        break
print(res)
