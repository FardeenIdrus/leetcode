from collections import defaultdict
class Solution:
    def isValidSudoku(self, board:list[list[str]]) -> bool:
        
        # Initialise dictionary - key: box identifier (tuple), value: numbers seen in that box
        boxes = defaultdict(set)
        
        # Initialise dictonary - key: row index, value: numbers seen in that row
        row_dict = defaultdict(set)
        
        # Initialise dictionary - key: column index, value: numbers seen in that column
        column_dict = defaultdict(set)
        
        # Loop through each cell in the board
        for row in range(len(board)):
            for column in range(len(board[0])):
                # Obtain the number in the current cell
                digit = board[row][column]
                # Check whether the number is already present in the current row or current column (across the entire board)
                # If yes - return False - invalid
                if digit != ".":
                    if digit in row_dict[row] or digit in column_dict[column]:
                        return False
                    
                    # If no - add the number to the row and column dictionary, so that if the same number appears
                    # in the same row or column in future cells - we return False
               
                    row_dict[row].add(digit), column_dict[column].add(digit)
                    
                    # Obtain which box the cell belongs to - using floor division.
                    # Each cell in the same box will have the same tuple
                    # E.g) Cells Row :1, Column 1, and Row :2 , Column: 2 will have the tuples (0,0) indicating that they
                    # are in the same sub-box
                    box = tuple([row//3, column//3])  
                    # Check whether that number has already appeared in the sub-box
                    # If yes, return False
                    if digit in boxes[box]:
                        return False
                    # If no, add the number to the sub-box dictionary - so that duplicates are flagged as invalid
                    else:
                         boxes[box].add(digit)
                              
        
        return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
    
    print(sol.isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
    
# Time complexity: O(n^2) -> where n is the length of one side of the grid. 
# Every cell is visited exactly once, giving n^2 total cells checked.
# For each cell, the lookups and inserts into row_dict, column_dict, and boxes are all O(1) average, since dictionaries are hash-based. 
# So the total work scales with the number of cells : O(n^2)

# Space complexity: O(n^2), where n is the side length of the grid
# 3 Hash-map strucutres are used 
# row_dict holds one set per row, column_dict holds one set per column and bxoes holds one set per 3x3 sub-box
# In the worst case (a fully filled, valid board), each structure together stores up to n^2 digits total, since every cell contributes one digit
# to exactly one row set, one column-set, and one box-set