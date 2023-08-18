# Technique: Trie as a parameter

# Time Complexity: O(n * m * word_length * 8^word_length) where n and m are dimensions of the board
# Space Complexity: O(word_length + n*m) 

from Trie import Trie, TrieNode

def boggle(board, dictionary):
    # Build Trie
    trie = Trie()
    for word in dictionary:
        trie.insert(word)
    trie_root = trie.root

    rows, cols = len(board), len(board[0])
    res = set()

    def backtrack(row, col, curr_node, path, visited):
        if curr_node.validWord and len(path) >= 3:
            res.add(path)
        
        for (i, j) in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            newRow, newCol = row + i, col + j
            if 0 <= newRow < rows and 0 <= newCol < cols and (newRow, newCol) not in visited:
                char = board[newRow][newCol]
                child = curr_node.children[ord(char) - ord('a')]
                if child:
                    backtrack(newRow, newCol, child, path + char, visited | {(newRow, newCol)})

    for row in range(rows):
        for col in range(cols):
            char = board[row][col]
            child = trie_root.children[ord(char) - ord('a')]
            if child:
                backtrack(row, col, child, char, {(row, col)})

    return list(res)

dictionary = ["ace", "ape", "cape", "clap", "clay", "gape", "grape", "lace", "lap", "lay", "mace", "map", "may", "pace", "pay", "rap", "ray", "tap", "tape", "trace", "trap", "tray", "yap", "race"]
board = [
    ['a', 'd', 'e'],
    ['r', 'c', 'p'],
    ['l', 'a', 'y']
]

result = boggle(board, dictionary)
expected_output = ["ace", "race", "pace", "lace", "pay", "lay", "clay", "ray", "lap", "rap", "clap", "ape", "cape", "yap"]
assert set(result) == set(expected_output)

dictionary2 = ["test", "tea", "tease", "seat", "eat", "ate"]
board2 = [
    ['e', 'a', 't'],
    ['e', 's', 't'],
    ['e', 'a', 't']
]
result2 = boggle(board2, dictionary2)
expected_output2 = ["seat", "eat"]
assert set(result2) == set(expected_output2)

dictionary3 = ["board", "bore", "rode", "road", "bad", "dare", "bare", "read", "bade"]
board3 = [
    ['b', 'o', 'a', 'r'],
    ['d', 'r', 'e', 'd']
]
result3 = boggle(board3, dictionary3)
expected_output3 = ['bore', 'dare', 'read', 'board', 'road']
print(result3)
assert set(result3) == set(expected_output3)




# Time Taken - 35 minutes