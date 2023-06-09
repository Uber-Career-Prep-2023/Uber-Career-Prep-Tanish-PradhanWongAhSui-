from collections import deque

def numIslands(matrix: list[list[int]])-> int:
    # bfs approach
    # time - O(m*n), space - O(m*n)
    count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1:
                count += 1
                queue = deque([(row, col)])
                while queue:
                    coord = queue.popleft()
                    r, c = coord[0], coord[1]
                    if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]):
                        continue
                    if matrix[r][c] == 1:
                        matrix[r][c] = 0
                        queue.append((r+1, c))
                        queue.append((r-1, c))
                        queue.append((r, c+ 1))
                        queue.append((r, c-1))
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

# took 25 minutes