# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        currDepth = 0
        return self.maxDepthHelper(root,currDepth)
    
    def maxDepthHelper(self,node,currDepth):
        if node is None:
            return currDepth
        currDepth += 1
        
        depth_left = self.maxDepthHelper(node.left,currDepth)
        depth_right = self.maxDepthHelper(node.right,currDepth)
        
        return max(depth_left,depth_right)