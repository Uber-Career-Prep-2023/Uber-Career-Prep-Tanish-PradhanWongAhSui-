# Technique: Dynamic programming
# Time complexity: O(len(coins) * target_sum)
# Space complexity: O(target_sum)

def coinChange(coins, sum):
    dp = [0] * (sum + 1)
    dp[0] = 1
    
    for coin in coins:
        for j in range(coin, sum + 1):
            dp[j] += dp[j - coin]
            
    return dp[sum]

coins = [2, 5, 10]
assert coinChange(coins, 20) == 6
assert coinChange(coins, 15) == 3

assert coinChange([], 20) == 0  
assert coinChange(coins, 0) == 1  
assert coinChange([2, 4], 7) == 0  
assert coinChange([1], 100) == 1  
assert coinChange([3, 6, 9], 18) == 7

assert coinChange([2, 3, 5], 8) == 3 
assert coinChange([1, 2, 3], 4) == 4  


# Approximate time taken: 30 minutes
