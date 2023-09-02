class TrieNode:
    def __init__(self):
        # time - O(1)
        # space - O(1)
        self.children = [None] * 26  
        self.validWord = False

class Trie:
    def __init__(self):
        # time - O(1)
        # space - O(1)
        self.root = TrieNode()

    def insert(self, word):
        # time - O(n) 
        # space - O(1)
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.validWord = True

    def isValidWord(self, word):
        # time - O(n) 
        # space - O(1)
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not node.children[index]:
                return False
            node = node.children[index]
        return node.validWord

    def remove(self, word):
        # time - O(n)
        # space - O(1)
        def _delete(node, word, depth):
            if not node:
                return False
            if depth == len(word):
                if node.validWord:
                    node.validWord = False
                    return not any(node.children)
            else:
                index = ord(word[depth]) - ord('a')
                if _delete(node.children[index], word, depth+1):
                    del node.children[index]
                    node.children[index] = None
                    return not node.validWord and not any(node.children)
            return False

        _delete(self.root, word, 0)

trie = Trie()
trie.insert('apple')
assert trie.isValidWord('apple') == True

trie = Trie()
trie.insert('apple')
trie.insert('app')
trie.remove('apple')
assert trie.isValidWord('apple') == False
assert trie.isValidWord('app') == True

trie = Trie()
trie.insert('apple')
trie.remove('app')
assert trie.isValidWord('apple') == True
assert trie.isValidWord('app') == False

trie = Trie()
trie.insert('apple')
trie.insert('app')
trie.remove('apple')
trie.remove('app')
assert trie.isValidWord('apple') == False
assert trie.isValidWord('app') == False

trie = Trie()
assert not trie.isValidWord("")

# took about 35 minutes
