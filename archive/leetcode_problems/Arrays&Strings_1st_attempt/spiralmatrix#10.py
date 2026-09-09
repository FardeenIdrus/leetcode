
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        top_row = 0
        bottom_row = len(matrix)-1
        left_column = 0
        right_column = len(matrix[0])-1
        matrix_elements = []
        while top_row <= bottom_row and left_column <= right_column:
            
            #Append felements in irst row 
            for i in range(left_column, right_column+1):
                matrix_elements.append(matrix[top_row][i])
                
            #First row visited so we move the row wall down
            top_row +=1
            
            # Append elements in the right most column moving down
            for i in range(top_row, bottom_row+1):
                matrix_elements.append(matrix[i][right_column])
            
            # Right most column visited, so we move the right column wall to the left
            right_column -=1
            
            
            # Bottom row may already be visited - only traverse if rows remain
            if top_row <= bottom_row:
                
            # Append elements in the bottom row moving left
                for i in range(right_column, left_column-1, -1):
                    # Append elements in the left most column moving up
                    matrix_elements.append(matrix[bottom_row][i])
                    
                bottom_row -=1
            
            
            # Left column may already be visited - only travese if column remains 
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