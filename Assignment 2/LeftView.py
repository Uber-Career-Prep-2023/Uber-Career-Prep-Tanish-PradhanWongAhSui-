# uses level order- breadth first traversal
# Time complexity - O(n)
# Space complexity - O(h) 

from BinarySearchTree import TreeNode

def leftview(root: TreeNode) -> list:
    if not root:
        return []
    res = []
    level = [root]
    while level:
        new_level = []
        res.append(level[-1].val)
        for i in level:
            if i.right:
                new_level.append(i.right)
            if i.left:
                new_level.append(i.left)
        level = new_level
    return res

tree1 = TreeNode(7)
tree1.left = TreeNode(8)
tree1.right = TreeNode(3)
tree1.right.left = TreeNode(9)
tree1.right.right = TreeNode(13)
tree1.right.left.left = TreeNode(20)
tree1.right.right.left = TreeNode(14)
tree1.right.right.left.right = TreeNode(15)
assert leftview(tree1) == [7, 8, 9, 20, 15]

tree2 = TreeNode(7)
tree2.left = TreeNode(20)
tree2.right = TreeNode(4)
tree2.left.right = TreeNode(6)
tree2.left.left = TreeNode(15)
tree2.right.right = TreeNode(11)
tree2.right.left = TreeNode(8)
assert leftview(tree2) == [7,20,15]

assert leftview(None) == []

root = TreeNode(5)
assert leftview(root) == [5]

root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)
assert leftview(root) == [1, 2, 3, 4]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
assert leftview(root) == [1, 2, 4]

root = TreeNode(-1)
root.left = TreeNode(-12312)
root.right = TreeNode(3)
root.left.left = TreeNode(-54)
root.left.right = TreeNode(5)
root.right.left = TreeNode(-6)
root.right.right = TreeNode(7)
assert leftview(root) == [-1, -12312, -54]

# took 22 minutes