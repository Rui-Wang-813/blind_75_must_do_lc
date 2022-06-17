# solution by Rui Wang
# problem description link: https://leetcode.com/problems/same-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None or q == None:
            return p == None and q == None
        
        if p.val != q.val:
            return False
        
        if not self.isSameTree(p.left, q.left):
            return False
        
        return self.isSameTree(p.right, q.right)