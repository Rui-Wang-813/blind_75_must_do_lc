# solution by Rui Wang
# problem description: https://leetcode.com/problems/rotate-image/

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        
        # iterate from first layer to the inner most layer (1 layer is the 4 sides of a square)
        # there are at most N//2 layers. If there are only odd number of items in the first,
        # then there is only one item in the inner most layer.
        n = 0
        while n < N // 2:
            itemNum = N - n * 2
            temp = matrix[n][n:n+itemNum]   # array called temp to store the temperary values in rotation.
            
            irow = icol = n
            
            i = 0
            # iterate through all items of one side. There are only four sides, so in each iteration I 
            # perform 4 swap options in the corresponding positions.
            while i < itemNum - 1:
                matrix[irow+i][icol+itemNum-1], temp[i] = temp[i], \
                matrix[irow+i][icol+itemNum-1]
                
                matrix[irow+itemNum-1][icol+itemNum-i-1], temp[i] = temp[i], \
                matrix[irow+itemNum-1][icol+itemNum-i-1]
                
                matrix[irow+itemNum-i-1][icol], temp[i] = temp[i], \
                matrix[irow+itemNum-i-1][icol]
                
                matrix[irow][icol+i] = temp[i]
                
                i += 1
            
            n += 1
    
    def printMatrix(self, matrix):
        for row in matrix:
            print(row)
        print()

sol = Solution()
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
sol.printMatrix(matrix)
sol.rotate(matrix)
sol.printMatrix(matrix)