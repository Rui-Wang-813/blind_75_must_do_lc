# solution by Rui Wang
# problem description link: https://leetcode.com/problems/word-search/

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(word) == 0:
            return True
        
        def helper(i, j, w_idx):
            if w_idx == len(word):
                return True
            
            c = word[w_idx]
            
            if i > 0 and (i-1, j) not in visited:
                if board[i-1][j] == c:
                    visited.add((i-1, j))
                    if helper(i-1, j, w_idx+1):
                        return True
                    visited.remove((i-1, j))
            
            if j > 0 and (i, j-1) not in visited:
                if board[i][j-1] == c:
                    visited.add((i, j-1))
                    if helper(i, j-1, w_idx+1):
                        return True
                    visited.remove((i, j-1))
            
            if i < len(board) - 1 and (i+1, j) not in visited:
                if board[i+1][j] == c:
                    visited.add((i+1, j))
                    if helper(i+1, j, w_idx+1):
                        return True
                    visited.remove((i+1, j))
            
            if j < len(board[0]) - 1 and (i, j+1) not in visited:
                if board[i][j+1] == c:
                    visited.add((i, j+1))
                    if helper(i, j+1, w_idx+1):
                        return True
                    visited.remove((i, j+1))
            
            return False
        
        visited = set()
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    visited.add((i, j))
                    if helper(i, j, 1):
                        return True
                    visited.remove((i, j))
        
        return False