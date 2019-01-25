def solution(coins, amount):
    coins = sorted(coins)
    minCoins = [0] * (amount + 1)

    for k in range(1, amount+1):
        minCoins[k] = amount + 1
        i = 0
        while i < len(coins) and coins[i] <= k:
            minCoins[k] = min(minCoins[k], minCoins[k - coins[i]] + 1)
            i += 1

    if minCoins[amount] == amount + 1:
        return -1
    else:
        return minCoins[amount]


coins = [2, 4, 8, 16]
amount = 100
print(solution(coins, amount))