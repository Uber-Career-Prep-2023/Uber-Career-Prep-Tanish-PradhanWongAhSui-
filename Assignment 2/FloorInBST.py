# Uses search binary search tree (BST)
# Time complexity - O(h) which is O(logn) for balanced tree and O(n) for completely unbalanced tree
# Space complexity - O(1)
from BinarySearchTree import TreeNode

def floor(root: TreeNode, target: int) -> int:
    output = None
    while root:
        if root.val <= target:
            output = root.val
            root = root.right
        else:
            root = root.left
    return output

test_tree1 = TreeNode(10)
test_tree1.right = TreeNode(16)
test_tree1.right.left = TreeNode(13)
test_tree1.right.right = TreeNode(17)
test_tree1.right.right.right = TreeNode(20)
test_tree1.left = TreeNode(8)
test_tree1.left.right = TreeNode(9)

assert floor(test_tree1, 13) == 13
assert floor(test_tree1, 15) == 13
assert floor(test_tree1, 18) == 17

test_tree2 = TreeNode(10)
test_tree2.right = TreeNode(16)
test_tree2.right.left = TreeNode(13)
test_tree2.right.left.right = TreeNode(15)
test_tree2.right.left.left = TreeNode(14)
test_tree2.right.right = TreeNode(17)
test_tree2.right.right.right = TreeNode(20)
test_tree2.left = TreeNode(8)
test_tree2.left.right = TreeNode(9)

assert floor(test_tree2, 13) == 13
assert floor(test_tree2, 15) == 15
assert floor(test_tree2, 18) == 17

assert floor(None, 1212) == None
assert floor(test_tree2, -1) == None
assert floor(test_tree2, 100000) == 20

test_tree3 = TreeNode(100)
test_tree3.left = TreeNode(90)
test_tree3.left.left = TreeNode(89)
test_tree3.left.left.left =TreeNode(70)
test_tree3.left.left.left.left = TreeNode(30)

assert floor(test_tree3, 120) == 100
assert floor(test_tree3, 90) == 90
assert floor(test_tree3, 99) == 90
assert floor(test_tree3, 60) == 30
assert floor(test_tree3, 70) == 70
assert floor(test_tree3, 88) == 70
assert floor(test_tree3, 19) == None

assert floor(None, 5) == None

root = TreeNode(3)
assert floor(root, 5) == 3

root = TreeNode(10)
assert floor(root, 5) == None

root = TreeNode(8)
root.left = TreeNode(4)
root.right = TreeNode(12)
root.left.left = TreeNode(2)
root.left.right = TreeNode(6)
root.right.left = TreeNode(10)
root.right.right = TreeNode(14)

assert floor(root, 5) == 4
assert floor(root, 12) == 12
assert floor(root, 7) == 6
assert floor(root, 15) == 14

root = TreeNode(-10)
root.left = TreeNode(-20)
root.right = TreeNode(0)
root.left.left = TreeNode(-30)
root.right.left = TreeNode(-2)
root.right.left.left = TreeNode(-5)
root.right.right = TreeNode(5)

assert floor(root, -4) == -5
assert floor(root, -31) == None
assert floor(root, -8) == -10
assert floor(root, -1) == -2

root = TreeNode(5)
root.left = None
root.right = TreeNode(10)
root.right.left = None
root.right.right = TreeNode(15)

assert floor(root, 5) == 5
assert floor(root, 7) == 5
assert floor(root, 12) == 10
assert floor(root, 20) == 15

# took 25 minutes