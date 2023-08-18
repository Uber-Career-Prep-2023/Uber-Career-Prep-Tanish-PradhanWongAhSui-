# Technique: Dynamic programming - tabulation
# Time complexity: O(n)
# Space complexity: O(n)

def minCostStairClimbing(costs):
    n = len(costs)
    if n == 1: return costs[0]
    if n == 2: return min(costs)
    
    dp = [0] * n
    dp[0], dp[1] = costs[0], costs[1]
    
    for i in range(2, n):
        dp[i] = costs[i] + min(dp[i-1], dp[i-2])
        
    return min(dp[-1], dp[-2])

# Test Cases
assert minCostStairClimbing([4, 1, 6, 3, 5, 8]) == 9
assert minCostStairClimbing([11, 8, 3, 4, 9, 13, 10]) == 25
assert minCostStairClimbing([1]) == 1
assert minCostStairClimbing([5, 3]) == 3
assert minCostStairClimbing([8, 5, 3, 7, 10]) == 12
assert minCostStairClimbing([5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 125
assert minCostStairClimbing([10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 50
assert minCostStairClimbing([10, 10]) == 10
assert minCostStairClimbing([100]) == 100
assert minCostStairClimbing([5, 1, 1, 5]) == 2

# Approximate time taken: 25 minutes.
