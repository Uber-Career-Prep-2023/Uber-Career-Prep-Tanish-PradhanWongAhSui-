class TreeNode:
    def __init__(self, val: int):
        # O(1)
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

class BinarySearchTree:
    def __init__(self):
        # O(1)
        self.root = None

    def min(self):
        # O(h) -> h is the height of the tree
        if not self:
            return
        curr = self.root
        while curr.left:
            curr = curr.left
        return curr.val

    def max(self):
        # O(h) 
        if not self:
            return 
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr.val

    def contains(self, val: int) -> bool:
        # O(h)
        curr = self.root
        while curr:
            if curr.val > val:
                curr = curr.left
            elif curr.val < val:
                curr = curr.right
            else:
                return True
        return False

    def insert(self, val: int):
        # O(h)
        # This assumes if a node with the given value already exists, it does not add it again.
        new_node = TreeNode(val)
        if not self.root:
            self.root = new_node
            return
        curr = self.root
        while True:
            if curr.val == val:
                return
            if val > curr.val:
                if not curr.right:
                    curr.right = new_node
                    return
                curr = curr.right
            else:
                if not curr.left:
                    curr.left = new_node
                    return
                curr = curr.left

    def delete(self, val):
        # Time and space complexity both O(h)
        if not self:
            return None
        
        if self.val == val:
            if not self.right: return self.left
            elif not self.left: return self.right
            
            curr = self.right
            while curr.left:
                curr = curr.left
            self.val = curr.val
            self.right = self.delete(self.right, val)
        
        elif val > self.val:
            self.right = self.delete(self.right, val)
        else:
            self.left = self.delete(self.left, val)
        return self




