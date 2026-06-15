from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # Four boundaries that shrink inward as we peel off each ring
        top_row = 0 
        bottom_row = len(matrix) - 1
        left_column = 0
        right_column = len(matrix[0]) - 1
        matrix_elements = []
        
        # Keep peeling rings while there's still an unvisited area inside
        while top_row <= bottom_row and left_column <= right_column:
            
            # 1. Traverse top row left to right
            for i in range(left_column, right_column + 1):
                matrix_elements.append(matrix[top_row][i])
            top_row += 1  # top row done, move boundary down
            
            # 2. Traverse right column top to bottom
            for i in range(top_row, bottom_row + 1):
                matrix_elements.append(matrix[i][right_column])
            right_column -= 1  # right column done, move boundary left
            
            # 3. Traverse bottom row right to left
            # Guard: skip if top and bottom were the same row originally
            # (the first loop already covered it)
            if top_row <= bottom_row:
                for i in range(right_column, left_column - 1, -1):
                    matrix_elements.append(matrix[bottom_row][i])
                bottom_row -= 1  # bottom row done, move boundary up
            
            # 4. Traverse left column bottom to top
            # Guard: skip if left and right were the same column originally
            # (the second loop already covered it)
            if left_column <= right_column:
                for i in range(bottom_row, top_row - 1, -1):
                    matrix_elements.append(matrix[i][left_column])
                left_column += 1  # left column done, move boundary right
        
        return matrix_elements
    


if __name__ == "__main__":
    sol = Solution()
    print(sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
    print(sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
    
    