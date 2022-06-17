# solution by Rui Wang
# problem description link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # note that this solution only works if the tree node values are unique. (gauranteed in the question
    # description)
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        
        rootVal = preorder[0]
        
        idx_root_inorder = inorder.index(rootVal)
        
        left_preorder = preorder[1:1+idx_root_inorder]
        left_inorder = inorder[:idx_root_inorder]
        
        right_preorder = preorder[1+idx_root_inorder:]
        right_inorder = inorder[idx_root_inorder+1:]
        
        root = TreeNode(rootVal)
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        
        return root