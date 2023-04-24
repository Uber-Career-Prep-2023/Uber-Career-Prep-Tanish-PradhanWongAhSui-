class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

def copyTree(root: TreeNode) -> TreeNode:
    # Time complexity - O(n)
    # Space complexity - O(n)
    if not root:
        return None
    new_node = TreeNode(root.val)
    new_node.left = copyTree(root.left)
    new_node.right = copyTree(root.right)
    
    return new_node

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

new_root = copyTree(root)

assert new_root.val == root.val
assert new_root.left.val == root.left.val
assert new_root.right.val == root.right.val
assert new_root.left.left.val == root.left.left.val
assert new_root.left.right.val == root.left.right.val