# Engin Yüksel
# 4.02.2021 10:03
# https://projecteuler.net/problem=29

myList = []
for i in range(2, 101):
    for j in range(2, 101):
        res = i ** j
        if res not in myList:
            myList.append(res)

print(len(myList))
