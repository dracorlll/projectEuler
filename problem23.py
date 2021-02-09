# Engin Yüksel
# 31.01.2021 23:13
# https://projecteuler.net/problem=23

def divisor(num):
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)

    return sum(divisors)


abundant = []
total = []
for i in range(12, 28123):
    if i < divisor(i):
        abundant.append(i)

for i in range(len(abundant)):
    for j in range(i, len(abundant)):
        asd = abundant[i] + abundant[j]
        if asd < 28123:
            total.append(asd)

total = list(dict.fromkeys(total))
total = sum(total)
print(28122*28123/2 - total)

