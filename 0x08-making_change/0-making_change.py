#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0

    database = [float('inf')] * (total + 1)
    database[0] = 0

    for quantity in range(1, total + 1):
        for coin in coins:
            if coin <= quantity:
                database[quantity] = min(database[quantity], database[quantity - coin] + 1)

    return database[total] if database[total] != float('inf') else -1
