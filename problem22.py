# Engin Yüksel
# 31.01.2021 22:38
# https://projecteuler.net/problem=22

names = open("p022_names.txt", "r")
names = names.read().replace("\"", "").split(",")

names.sort()
total = 0

for i in range(len(names)):
    alphavalue = 0
    for j in range(len(names[i])):
        alphavalue += ord(names[i][j]) - 64
    total += alphavalue * (i + 1)

print(total)

