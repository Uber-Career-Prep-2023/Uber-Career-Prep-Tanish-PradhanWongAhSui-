# Technique: Memoization
# Time complexity: O(n^2)
# Space complexity: O(n)

def factorial(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 1
    memo[n] = n * factorial(n-1, memo)
    return memo[n]

def catalan_numbers(n):
    catalan = [0] * (n+1)
    catalan[0] = 1
    for i in range(1, n+1):
        catalan[i] = (factorial(2*i) // (factorial(i+1) * factorial(i)))
    return catalan

# Test Cases
assert catalan_numbers(1) == [1, 1]
assert catalan_numbers(5) == [1, 1, 2, 5, 14, 42]
assert catalan_numbers(0) == [1]
assert catalan_numbers(3) == [1, 1, 2, 5]
assert catalan_numbers(4) == [1, 1, 2, 5, 14]
assert catalan_numbers(6) == [1, 1, 2, 5, 14, 42, 132]

# Approximate time taken: 20 minutes.
