# solution by Rui Wang
# problem description link: https://leetcode.com/problems/validate-binary-search-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(subRoot, lb, ub):
            if subRoot == None:
                return True
            
            if subRoot.val <= lb or subRoot.val >= ub:
                return False
            
            a = helper(subRoot.left, lb, subRoot.val)
            if not a:
                return False
            
            b = helper(subRoot.right, subRoot.val, ub)
            
            return b
        
        return helper(root, float('-inf'), float('inf'))