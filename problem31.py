# Engin Yüksel
# 4.02.2021 11:24
# https://projecteuler.net/problem=31


coins = [200, 100, 50, 20, 10, 5, 2, 1]


def combi(amount, coin):
    if amount == 0:
        return 1

    if amount < 0:
        return 0
    counter = 0
    for i in range(coin, len(coins)):
        counter += combi(amount - coins[i], i)
    return counter


print(combi(200, 0))
