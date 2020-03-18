# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        if not p and not q:
            return True
        if not q or not p:
            return False
        
        tree_one_array = []
        tree_two_array = []
        
        self.bfs(p,tree_one_array)
        self.bfs(q,tree_two_array)
        
        print(tree_one_array)
        print(tree_two_array)
        
        return tree_one_array == tree_two_array
    
    
        
    def bfs(self,node,tree_array):
        
        Queue = deque()
        Queue.append(node)
        
        while len(Queue) != 0:
            
            curr_element = Queue.popleft()
            if curr_element is not None:
                tree_array.append(curr_element.val)
                if curr_element.left is not None:
                    Queue.append(curr_element.left)
                elif curr_element.left is None and curr_element.right is not None:
                    tree_array.append(None)
                if curr_element.right is not None:
                    Queue.append(curr_element.right)
            
        
            
        
        