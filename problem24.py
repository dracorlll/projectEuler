# Engin Yüksel
# 1.02.2021 03:42
# https://projecteuler.net/problem=24

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

counter = 1
while True:
    if counter == 1000000:
        num = ""
        for i in range(len(arr)):
            num += str(arr[i])
        print(num)
        break
    k = 0
    L = 0
    for i in range(8, -1, -1):
        if arr[i] < arr[i + 1]:
            k = i
            break
        else:
            k = 99

    if k == 99:
        break

    for i in range(9, -1, -1):
        if arr[k] < arr[i]:
            L = i
            break
    arr[k], arr[L] = arr[L], arr[k]

    reverseList = []
    for i in range(k + 1, len(arr)):
        reverseList.append(arr[i])
    for i in range(len(arr) - 1, k, -1):
        arr.pop(i)

    reverseList.reverse()
    arr.extend(reverseList)

    counter += 1
