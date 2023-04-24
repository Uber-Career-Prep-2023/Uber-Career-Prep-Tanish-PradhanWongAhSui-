class TreeNode:
    def __init__(self, val: int):
        # O(1)
        self.val = val
        self.left = None
        self.right = None

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
        curr = self
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
        # first search for node
        curr = self.root
        while curr:
            if curr.val == val:
                break
            if curr.left:
                if curr.left.val == val and not curr.:

            elif curr.left > val:
                curr = curr.left
            else:
                curr = curr.right
        if not curr:
            return None
        if curr.le

        # case1 - node to delete has no left or right
        #   simply delete node
        # case2 - node to delete has one left or right
        #   shift up the left or right
        # case3 - node to delete has both left and right
        #   find next biggest element, replace node to delete's value with that and then delete that next biggest element


#    3
#  /  \ 
# 2    5
# 






