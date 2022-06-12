# solution by Rui Wang
# problem description link: https://leetcode.com/problems/spiral-matrix/

from typing import List

from numpy import mat

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        
        result = []
        
        i, j = 0, 0
        while m > 0 and n > 0:
            irow, icol = i, j
            
            while icol < j + n:
                result.append(matrix[irow][icol])
                icol += 1
            icol -= 1
            
            irow += 1
            while irow < i + m:
                result.append(matrix[irow][icol])
                irow += 1
            irow -= 1

            # in this case, the above two loops have done everything we need, and
            # the result is already completed.
            if m == 1 or n == 1:
                return result
            
            icol -= 1
            while icol >= j:
                result.append(matrix[irow][icol])
                icol -= 1
            icol += 1
            
            irow -= 1
            while irow > i:
                result.append(matrix[irow][icol])
                irow -= 1
            
            i += 1
            j += 1
            
            m -= 2
            n -= 2
        
        return result
    
    def printMatrix(self, matrix):
        for row in matrix:
            print(row)
        print()

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

sol = Solution()
sol.printMatrix(matrix)
print(sol.spiralOrder(matrix))