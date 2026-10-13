from collections import defaultdict
import itertools
class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        
        diagonal_sums= defaultdict(list)
        res = [] 

        for row in range(len(mat)):
            for column in range(len(mat[0])):
                cell_sum = row + column
                diagonal_sums[cell_sum].append(mat[row][column])

        
        for sum in diagonal_sums:
            if sum % 2== 0:
                diagonal_sums[sum].reverse()
            res.append(diagonal_sums[sum])
        
        return list(num for sublist in res for num in sublist)
    
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))