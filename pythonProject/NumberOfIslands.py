from collections import deque
def numIslands(matrix: list[list[int]]) -> int:
    if not matrix or not matrix[0]:
        return 0
    count = 0
    numrows = len(matrix)
    numcols = len(matrix[-1])
    for row in range(numrows):
        for col in range(numcols):
            if matrix[row][col] == 1:
                count += 1
                queue = deque([(row, col)])
                while queue:
                    curr = queue.popleft()
                    if curr[0] < 0 or curr[0] >= numrows or curr[1] < 0 or curr[1] >= numcols:
                        continue
                    if matrix[curr[0]][curr[1]] == 1:
                        matrix[curr[0]][curr[1]] = 0
                        queue.append((curr[0] + 1, curr[1]))
                        queue.append((curr[0] - 1, curr[1]))
                        queue.append((curr[0], curr[1] + 1))
                        queue.append((curr[0], curr[1] - 1))
    return count

matrix1 = [[1, 0, 1, 1, 1],
           [1, 1, 0, 1, 1],
           [0, 1, 0, 0, 0],
           [0, 0, 0, 1, 0],
           [0, 0, 0, 0, 0]]

matrix2 = [[1, 0, 0],
           [0, 0, 0]]

matrix3 = [ [1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1]]

matrix4 = [[0, 0, 0, 0],
           [0, 0, 0, 0]]

matrix5 = [[]]
matrix6 = []

matrix7 = [[1]]
matrix8 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

matrix9 = [[0, 0, 0],
           [0, 1, 0],
           [0, 0, 0]]

matrix10 = [[0, 0, 0],
           [0, 1, 0],
           [0, 0, 1]]

assert numIslands(matrix9) == 1
assert numIslands(matrix10) == 2
assert numIslands(matrix4) == 0
assert numIslands(matrix5) == 0
assert numIslands(matrix6) == 0
assert numIslands(matrix7) == 1
assert numIslands(matrix8) == 1
assert numIslands(matrix3) == 13
assert numIslands(matrix1) == 3
assert numIslands(matrix2) == 1

