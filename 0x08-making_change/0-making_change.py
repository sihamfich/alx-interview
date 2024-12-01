#!/usr/bin/python3
"""
Coin Change Problem Solution
"""

def makeChange(coins, total):
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if total == 0:
            break
        num_coins = total // coin
        count += num_coins
        total -= num_coins * coin

    # If there's a remaining total that cannot be made with given coins
    return -1 if total > 0 else count
