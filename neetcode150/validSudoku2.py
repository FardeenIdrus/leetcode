from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_dict = defaultdict(set)
        column_dict = defaultdict(set)
        box_dict = defaultdict(set)
        
        for row in range(9):
            for column in range(9):
                if board[row][column] != ".":
                    if board[row][column]  not in row_dict[row] and board[row][column] not in column_dict[column] and board[row][column] not in box_dict[(row//3, column//3)]:
                        row_dict[row].add(board[row][column]), column_dict[column].add(board[row][column]), box_dict[(row//3, column//3)].add(board[row][column])

                    else:
                        return False
        return True
         
#Time complexity: O(1): Board size remains constant
# Space complexity - O(1) - board size remains constant
# Each dicitonary with at most 9 keys, and each value is a set containing at most 9 numbers. 

if __name__ == "__main__":
    sol = Solution()
    print(sol.isValidSudoku([["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]))