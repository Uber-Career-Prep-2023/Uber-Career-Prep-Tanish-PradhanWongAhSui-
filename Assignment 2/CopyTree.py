# This approach uses the depth first tree traversal technique. It does this in the preorder traversal way but can be soled with any order traversal
# Time complexity - O(n)
# Space complexity - O(n) where h is the height of the tree
from BinarySearchTree import TreeNode

def copyTree(root: TreeNode) -> TreeNode:
    
    if not root:
        return None
    new_node = TreeNode(root.val)
    new_node.left = copyTree(root.left)
    new_node.right = copyTree(root.right)
    
    return new_node

root = TreeNode(1)
new_root = copyTree(root)
assert new_root.val == root.val

root = None
new_root = copyTree(root)
assert new_root == None

root = TreeNode(1)
root.left = TreeNode(2)
new_root = copyTree(root)
assert new_root.val == root.val
assert new_root.left.val == root.left.val


root = TreeNode(1)
root.right = TreeNode(2)
new_root = copyTree(root)
assert new_root.val == root.val
assert new_root.right.val == root.right.val


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
new_root = copyTree(root)
assert new_root.val == root.val
assert new_root.left.val == root.left.val
assert new_root.left.left.val == root.left.left.val

root = None
new_root = copyTree(root)
assert new_root is None

root = TreeNode(-1)
root.left = TreeNode(-2)
root.right = TreeNode(-3)
root.left.left = TreeNode(-4)
root.left.right = TreeNode(-5)

new_root = copyTree(root)

assert new_root.val == root.val
assert new_root.left.val == root.left.val
assert new_root.right.val == root.right.val
assert new_root.left.left.val == root.left.left.val
assert new_root.left.right.val == root.left.right.val

root10 = TreeNode(None)
new_root10 = copyTree(root10)

# took 15 minutes