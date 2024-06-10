#!/usr/bin/python3

"""
Making Change Problem Module

This module contains a function to determine the fewest number of coins needed to meet a given amount total.
"""

def make_change(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.
    
    Args:
        coins (list): A list of coin denominations.
        total (int): The total amount to make up.
        
    Returns:
        int: The fewest number of coins needed to meet the total amount, or -1 if it's impossible.
    """
    if total < 0:
        return -1

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

# Example usage:
if __name__ == "__main__":
    print(make_change([1, 2, 25], 37))  # Output: 7
    print(make_change([1256, 54, 48, 16, 102], 1453))  # Output: -1
