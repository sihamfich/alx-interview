#!/usr/bin/python3


def sieve_primes(limit):
    """Generate prime numbers up to a given
    limit using the Sieve of Eratosthenes."""
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for num in range(2, int(limit ** 0.5) + 1):
        if is_prime[num]:
            end = limit + 1
            step = num
            is_prime[num * num:end:step] = [False] * len(
                range(num * num, end, step)
            )
    return is_prime


def determine_winner_for_round(max_num):
    """Determine winner for a single round
    using primes and optimal strategy."""
    primes = sieve_primes(max_num)
    total_moves = sum(primes[:max_num + 1])
    return "Maria" if total_moves % 2 != 0 else "Ben"


def isWinner(num_rounds, round_limits):
    """Determine the overall winner for multiple rounds."""
    scores = {"Maria": 0, "Ben": 0}
    for limit in round_limits:
        winner = determine_winner_for_round(limit)
        scores[winner] += 1
    if scores["Maria"] > scores["Ben"]:
        return "Maria"
    elif scores["Ben"] > scores["Maria"]:
        return "Ben"
    return None
