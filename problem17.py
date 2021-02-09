# Engin Yüksel
# 30.01.2021 21:40
# https://projecteuler.net/problem=17

words = [0] * 100
words.insert(1, "ONE")
words.insert(2, "TWO")
words.insert(3, "THREE")
words.insert(4, "FOUR")
words.insert(5, "FIVE")
words.insert(6, "SIX")
words.insert(7, "SEVEN")
words.insert(8, "EIGHT")
words.insert(9, "NINE")
words.insert(10, "TEN")
words.insert(11, "ELEVEN")
words.insert(12, "TWELVE")
words.insert(13, "THIRTEEN")
words.insert(14, "FOURTEEN")
words.insert(15, "FIFTEEN")
words.insert(16, "SIXTEEN")
words.insert(17, "SEVENTEEN")
words.insert(18, "EIGHTEEN")
words.insert(19, "NINETEEN")
words.insert(20, "TWENTY")
words.insert(30, "THIRTY")
words.insert(40, "FORTY")
words.insert(50, "FIFTY")
words.insert(60, "SIXTY")
words.insert(70, "SEVENTY")
words.insert(80, "EIGHTY")
words.insert(90, "NINETY")
words.insert(100, "HUNDRED")


def placevalue(number):
    index = [int(number / 100)]
    number = number - index[0] * 100
    index.append(int(number / 10))
    number = number - index[1] * 10
    index.append(number)

    return index


result = 0
for i in range(1, 1000):
    number = ""
    index = placevalue(i)
    if index[0] != 0:
        if index[1] == 0 and index[2] == 0:
            number += words[index[0]] + " HUNDRED"
        else:
            number += words[index[0]] + " HUNDRED AND "
    if index[1] != 0 and index[1] != 1:
        number += words[index[1] * 10]
    if index[1] == 1:
        number += words[index[1] * 10 + index[2]]
    elif index[2] != 0:
        if index[1] == 0:
            number += words[index[2]]
        else:
            number += "-" + words[index[2]]

    print(str(i) + '.', number)
    number = number.replace(" ", "")
    number = number.replace("-", "")
    result += len(number)

print("1000. ONE THOUSAND")
# + one thousand - 11 letter
print(result + 11)
