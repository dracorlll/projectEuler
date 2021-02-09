# Engin Yüksel
# 31.01.2021 16:52
# https://projecteuler.net/problem=19

months = [
    31,
    28,
    31,
    30,
    31,
    30,
    31,
    31,
    30,
    31,
    30,
    31
]
# 1 jan 1900 Monday

days = 0
counter = 0
for i in range(1900, 2001):
    if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
        months.pop(1)
        months.insert(1, 29)
    else:
        months.pop(1)
        months.insert(1, 28)
    for j in range(12):
        if days % 7 == 6 and i != 1900:
            counter += 1
        days += months[j]
print(days)
print(counter)
