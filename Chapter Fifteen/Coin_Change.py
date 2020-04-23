# -*- coding: utf-8 -*-
def coin_change(coins: list, amount: int) -> int:
    ref = {0: 0}
    for j in range(1, amount + 1):
        tem = [float("inf")]
        for coin in coins:
            if j - coin >= 0:
                tem.append(ref[j - coin])
        n = min(tem) + 1
        ref[j] = n
    return ref[amount] if ref[amount] != float("inf") else -1


if __name__ == "__main__":
    print(coin_change([186, 419, 83, 408], 6249))
    print(coin_change([2], 3))
