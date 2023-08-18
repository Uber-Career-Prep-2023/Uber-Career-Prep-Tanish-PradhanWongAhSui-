# Technique: Dynamic programming
# Time complexity: O(n^2)
# Space complexity: O(n^2)

def largestSquareOf1s(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    n = len(matrix)
    dp = [[0] * n for _ in range(n)]
    largest_side = 0
    
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                largest_side = max(largest_side, dp[i][j])
                
    return largest_side

# Test Cases
matrix1 = [
    [0, 1, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 1]
]
assert largestSquareOf1s(matrix1) == 2

matrix2 = [
    [0, 1, 0, 1, 1],
    [0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 0, 0],
    [1, 1, 1, 0, 0]
]
assert largestSquareOf1s(matrix2) == 3

matrix3 = [
    [0, 1, 0, 1, 1],
    [0, 0, 1, 1, 1],
    [1, 1, 0, 1, 0],
    [1, 1, 1, 0, 0],
    [1, 1, 1, 0, 0]
]
assert largestSquareOf1s(matrix3) == 2

matrix4 = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
assert largestSquareOf1s(matrix4) == 0

matrix5 = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
]
assert largestSquareOf1s(matrix5) == 4

matrix6 = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
assert largestSquareOf1s(matrix6) == 3

matrix7 = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0]
]
assert largestSquareOf1s(matrix7) == 2

matrix8 = [
    [1]
]
assert largestSquareOf1s(matrix8) == 1

matrix9 = [
    [0]
]
assert largestSquareOf1s(matrix9) == 0

matrix10 = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]
assert largestSquareOf1s(matrix10) == 1

matrix11 = [
    []
]
assert largestSquareOf1s(matrix11) == 0


# Approximate time taken: 37 minutes.
