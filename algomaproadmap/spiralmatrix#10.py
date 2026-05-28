
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        top_row = 0
        bottom_row = len(matrix)-1
        left_column = 0
        right_column = len(matrix[0])-1
        matrix_elements = []
        while top_row <= bottom_row and left_column <= right_column:
            for i in range(left_column, right_column+1):
                matrix_elements.append(matrix[top_row][i])
            
            top_row +=1
            for i in range(top_row, bottom_row+1):
                matrix_elements.append(matrix[i][right_column])
            
            right_column -=1
            
            
            if top_row <= bottom_row:
                
                for i in range(right_column, left_column-1, -1):
                    matrix_elements.append(matrix[bottom_row][i])
                    
                bottom_row -=1
            
            if left_column <= right_column:
                    
                for i in range(bottom_row, top_row-1,-1):
                    matrix_elements.append(matrix[i][left_column])
                left_column +=1

        return matrix_elements
    
# Time complexity: O(m x n)
#Space ccomplexity:  O(1) excluding output, including O(mx n) 

if __name__ =="__main__":
    sol = Solution()
    #print(sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
    print(sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))