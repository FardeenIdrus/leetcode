from typing import List

class Solution:
    def rotate(self, matrix: List[List]) -> None:
        
        
    # Step 1: Transpose the matrix
    # Transpose means swap matrix[i][j] with matrix[j][i] for all cells above the diagonal
    # We only iterate cells where j > i to avoid swapping each pair twice
    
        for i in range(len(matrix)):
            # j starts at i+1 to skip the diagonal and only visit upper triangle
            for j in range(i+1, len(matrix)):
                # Swap the cell with its transposed counterpart
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
    # Step 2: Reverse each row
        for i in range(len(matrix)): 
            matrix[i].reverse()
        

        
if __name__ == "__main__":
    sol = Solution()
    print(sol.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))


# Time complexity:

# Step 1: Transpose
# Total iterations of inner loop across all i:
# When i=0: j runs (n-1) times
# When i=1: j runs (n-2) times
# ...
# When i=n-1: j runs 0 times
# Sum: (n-1) + (n-2) + ... + 1 + 0 = n(n-1)/2
# Drop constants: O(n^2)

# Step 2: Reverse each row
# Outer loop runs n times (once per row)
# Each .reverse() call on a row of length n takes O(n)
# Total: n rows × n operations per row = n^2 = O(n^2)

# Total: O(n^2) + O(n^2) = O(n^2)

#Space Complexity: O(1) - modifying matrix IN-PLACE. So no new data structres that grow with input size.