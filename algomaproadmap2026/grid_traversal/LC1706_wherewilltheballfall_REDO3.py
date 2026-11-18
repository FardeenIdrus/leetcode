class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:

        answer = [0] * len(grid[0])

        def dfs(row: int, col: int) -> int:
            
            # If the ball's row is greater than the number of rows in the grid, the ball has succesfull fell through the entire board
            if row == len(grid):
                return col
        
            elif 0<= row < len(grid) and 0<= col < len(grid[0]):
                # If the board pushes the ball to the right, check that the board does not push it against a wall or the board in cell col +1 is not pushing it to the left (v-shape pattern)
                if grid[row][col] == 1:
                    # len(grid[0))-1 because of 0-indexing. So if len(grid[0]) = 6, and the ball is on col = 5 (the last column), a board pushing it to the right is pushing it against a wall
                    if col+1 >= len(grid[0])  or grid[row][col+1] == -1:
                        col = -1
                    else:
                        row +=1
                        col +=1
                        return dfs(row, col)
                else:
                # If the board pushes the ball to the left, check that the board does not push it against a wall or the board in cell col -1 is not pushing it to the right (v-shape pattern)
                    if col-1 < 0 or grid[row][col-1] == 1:
                        col = -1
                    
                    else:
                        row +=1
                        col -=1
                        return dfs(row, col)

            return col

        for column in range(len(grid[0])):
            answer[column] = dfs(0, column)
        

        return answer

# Time Complexity: O(N x M) where N is the number of rows and M the number of columns
    # The for loop runs M times, where M is the number of columns in grid -> O(M)
    # Each column can make up to N+1 recursive calls, where N is the number of rows -> O(N+1) which simplifies to O(N)
        # N+1, because an additional recursive call is made when the ball is not stuck but on the last row of the grid, so the additional recursive call checks that the ball has succesfully exited
            # the grid. E.g) Board has 4 rows, and the ball is at (4,0), dfs(4,0) is called, and "if row == len(grid):"  branch is immediately executed
        # Each recursive call does O(1) work (lookup, comparison, and arithmetic, assignment)
        # O(N) * O(1) = O(N)
    # Each column can make up to N recursive calls, and there are M columns
    # Total = O(N) * O(M) = O(NxM)

# Space Complexity: O(N), where N is thenumber of rows 
    # Since the for loop checks one column in each iteration, there can be up to N+1 calls waiting on the call stack for each column
    # Calls for different columns are never stacked up together, because each ball's drop finishes before the next one starts
    # N+1 frames x O(1) per frame = O(N)
    # row, col, and column take constant space

    



