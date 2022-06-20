# solution by Rui Wang
# problem description link: https://leetcode.com/problems/binary-tree-maximum-path-sum/

from typing import Optional
from utils import TreeNode

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = float('-inf')
        
        # this helper function returns the largest path sum ending at subRoot.
        # and it updates the result if the max path sum including subRoot is larger.
        def searcher(subRoot):
            nonlocal result
            
            if subRoot == None:
                return 0
            
            leftSum = max(searcher(subRoot.left), 0)
            rightSum = max(searcher(subRoot.right), 0)
            
            result = max(result, leftSum + subRoot.val + rightSum)
            
            return max(leftSum, rightSum) + subRoot.val
        
        searcher(root)
        return result