# solution by Rui Wang
# problem description link: https://leetcode.com/problems/set-matrix-zeroes/

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        zero_set = set()
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_set.add((i, j))
        
        for i, j in zero_set:
            
            for icol in range(n):
                matrix[i][icol] = 0
            for irow in range(m):
                matrix[irow][j] = 0