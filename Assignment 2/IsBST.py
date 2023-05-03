# uses the generic depth-first traversal tree traversal technique
# time complexity - O(n)
# space complexity - O(h) - average case

import math
from BinarySearchTree import TreeNode

def isBST(root: TreeNode) -> bool:
    # this solution assumes that None does not count as a BST 
    if not root:
        return False
    def validBST(root: TreeNode, min: int, max: int):
        if not root:
            return True
        if root.val <= min or root.val >= max:
            return False
        return validBST(root.left, min, root.val) and validBST(root.right, root.val, max)
    return validBST(root, -math.inf, math.inf)
    
test1 = TreeNode(10)
test1.left = TreeNode(8)
test1.left.right = TreeNode(9)
test1.right = TreeNode(16)
test1.right.left = TreeNode(13)
test1.right.right = TreeNode(17)
test1.right.right.right = TreeNode(20)
assert isBST(test1) == True

test2 = TreeNode(10)
test2.left = TreeNode(8)
test2.left.right = TreeNode(9)
test2.right = TreeNode(16)
test2.right.left = TreeNode(13)
test2.right.right = TreeNode(17)
test2.right.right.right = TreeNode(15)
assert isBST(test2) == False

assert isBST(TreeNode(0)) == True
assert isBST(None) == False

test3 = TreeNode(12)
test3.right = TreeNode(14)
assert isBST(test3) == True

test4 = TreeNode(10)
test4.left = TreeNode(5)
assert isBST(test4) == True

test5 = TreeNode(120)
test5.left = TreeNode(121)
assert isBST(test5) != True

test6 = TreeNode(120)
test6.right = TreeNode(-10)
assert isBST(test6) == False

test7 = TreeNode(10)
test7.left = TreeNode(8)
test7.right = TreeNode(20)
test7.right.left = TreeNode(9)
test7.right.right = TreeNode(21)
assert isBST(test7) == False

test8 = TreeNode(10)
test8.left = TreeNode(2)
test8.right = TreeNode(10)
assert isBST(test8) == False

assert isBST(TreeNode(5)) == True

root = TreeNode(10)
root.left = TreeNode(8)
root.left.left = TreeNode(5)
root.left.right = TreeNode(9)
assert isBST(root) == True

root = TreeNode(10)
root.right = TreeNode(15)
root.right.left = TreeNode(13)
root.right.right = TreeNode(18)
assert isBST(root) == True

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(13)
root.right.right = TreeNode(18)
assert isBST(root) == True

root = TreeNode(10)
root.left = TreeNode(-5)
root.right = TreeNode(15)
root.right.left = TreeNode(13)
root.right.right = TreeNode(18)
assert isBST(root) == True

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.right.left = TreeNode(13)
root.right.right = TreeNode(25)
assert isBST(root) == True

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(10)
root.right.right = TreeNode(20)
assert isBST(root) == False

# took 30 minutes