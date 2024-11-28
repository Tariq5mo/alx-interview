#!/usr/bin/python3
"""
This module contains the makeChange function which calculates
the minimum number of coins needed to make a given amount of change.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Parameters:
    coins (list): A list of the values of the coins in your possession.
    total (int): The total amount of change needed.

    Returns:
    int: The fewest number of coins needed to meet the total.
    If the total cannot be met by any number of coins you have, return -1.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if total == 0:
            break
        if coin <= total:
            count += total // coin
            total %= coin

    return count if total == 0 else -1
