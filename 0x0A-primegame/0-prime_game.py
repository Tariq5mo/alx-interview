#!/usr/bin/python3
"""
This module contains functions to determine the winner of a prime game.
"""

from typing import List, Optional


def sieve(limit: int) -> List[int]:
    """
    Generate a list of primes up to limit using the Sieve of Eratosthenes.

    Args:
        limit (int): The upper limit to generate primes up to.

    Returns:
        List[int]: A list of prime numbers up to the limit.
    """
    is_prime = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if is_prime[p]:
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False
        p += 1
    return [num for num in range(2, limit + 1) if is_prime[num]]


def isWinner(rounds: int, numbers: List[int]) -> Optional[str]:
    """
    Determine the winner of the prime game.

    Args:
        rounds (int): The number of rounds to be played.
        numbers (List[int]): A list of integers representing
        the numbers for each round.

    Returns:
        Optional[str]: The name of the winner ("Maria" or "Ben"), or
        None if there is no winner.
    """
    if not numbers or rounds < 1:
        return None

    max_number = max(numbers)
    primes = sieve(max_number)

    maria_score = 0
    ben_score = 0

    for number in numbers:
        if number < 2:
            ben_score += 1
            continue

        prime_count = sum(1 for prime in primes if prime <= number)

        if prime_count % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1

    if maria_score > ben_score:
        return "Maria"
    elif ben_score > maria_score:
        return "Ben"
    else:
        return None
