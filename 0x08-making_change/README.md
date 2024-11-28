# Making Change

This project contains a function to determine the minimum number of coins needed to make a given amount of change.

## Function

### `makeChange(coins, total)`

This function calculates the minimum number of coins needed to make the given `total` amount using the denominations in the `coins` list.

#### Parameters

- `coins` (list): A list of coin denominations.
- `total` (int): The total amount of change needed.

#### Returns

- `int`: The minimum number of coins needed to make the change, or `-1` if it is not possible to make the change with the given denominations.

#### Example

```python
#!/usr/bin/python3
from 0-making_change import makeChange

print(makeChange([1, 2, 5], 11))  # Output: 3 (5 + 5 + 1)
print(makeChange([2], 3))         # Output: -1
```

## Usage

1. Ensure you have Python installed on your system.
2. Save the `0-making_change.py` file in your project directory.
3. Import and use the `makeChange` function in your Python script as shown in the example above.
