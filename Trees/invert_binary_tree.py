# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        # go to the left subtree, invert it
        # go to the right subtree, invert it
        # swap the links
        
        if root is None:
            return root
        
        if root.left is None and root.right is None:
            return root
        
        if root.left is not None:
            root.left = self.invertTree(root.left)
        
        if root.right is not None:
            root.right = self.invertTree(root.right)
        
        temp = root.left
        root.left = root.right
        root.right = temp
        
        return root