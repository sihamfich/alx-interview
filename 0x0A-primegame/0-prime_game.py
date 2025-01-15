#!/usr/bin/python3
""" Prime Game Module
"""


def isWinner(x: int, nums: list) -> str:
    """
    Determines the winner of a series of prime number games.

    Parameters:
    x (int): Number of rounds.
    nums (list): List of integers representing the upper limits for each round.

    Returns:
    str: Name of the winner ('Maria' or 'Ben'), or None if it's a tie.
    """
    if x < 1 or not nums:
        return None

    maria_score, ben_score = 0, 0

    # Create a sieve of Eratosthenes up to the largest number in nums
    max_num = max(nums)
    is_prime = [True] * (max_num + 1)
    is_prime[0] = False  # 0 is not a prime number
    is_prime[1] = False  # 1 is not a prime number

    for num in range(2, int(max_num**0.5) + 1):
        if is_prime[num]:
            for multiple in range(num * num, max_num + 1, num):
                is_prime[multiple] = False

    # Count primes for each round
    for i in range(x):
        n = nums[i]
        primes_up_to_n = sum(is_prime[:n + 1])
        if primes_up_to_n % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1

    if maria_score > ben_score:
        return "Maria"
    elif ben_score > maria_score:
        return "Ben"
    return None
