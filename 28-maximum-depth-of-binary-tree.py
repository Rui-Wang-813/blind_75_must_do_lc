# solution by Rui Wang
# problem description link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        frontier = [root]
        result = 0
        
        # use this to store how many nodes there are in each level.
        frontier_size = 1
        
        while len(frontier) != 0:
            new_frontier_size = 0   # layer_size for the next level.
            for _ in range(frontier_size):
                node = frontier.pop(0)
                
                if node.left != None:
                    frontier.append(node.left)
                    new_frontier_size += 1
                    
                if node.right != None:
                    frontier.append(node.right)
                    new_frontier_size += 1
            
            frontier_size = new_frontier_size
            result += 1
        
        return result