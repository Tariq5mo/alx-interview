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

    database = [float('inf')] * (total + 1)
    database[0] = 0

    for quantity in range(1, total + 1):
        for coin in coins:
            if coin <= quantity:
                database[quantity] = min(database[quantity],
                                         database[quantity - coin] + 1)

    return database[total] if database[total] != float('inf') else -1
