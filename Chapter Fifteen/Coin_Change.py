# -*- coding: utf-8 -*-
def coin_change(coins: list, amount: int) -> int:
    """
    ref = {0: 0}
    for j in range(1, amount + 1):
        n = float("inf")
        for i in range(1, j + 1):
            tem = [float("inf")]
            for coin in coins:
                if i - coin >= 0:
                    tem.append(ref[i - coin])
            n = min(tem) + 1
        ref[j] = n
    return ref[amount] if ref[amount] != float("inf") else -1
    """
    ref = {0: 0}

    def m_coin_change(c, a) -> int:
        if a in ref:
            return ref[a]
        n = float('inf')
        for _c in c:
            if a - _c >= 0:
                n = min(n, m_coin_change(c, a - _c) + 1)
        ref[a] = n
        return n

    res = m_coin_change(coins, amount)
    return res if res != float("inf") else -1


if __name__ == "__main__":
    print(coin_change([186, 419, 83, 408], 6249))
