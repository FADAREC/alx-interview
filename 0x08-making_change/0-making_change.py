#!/usr/bin/python3

def make_change(coins, total):
"""
Main file for testing
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
