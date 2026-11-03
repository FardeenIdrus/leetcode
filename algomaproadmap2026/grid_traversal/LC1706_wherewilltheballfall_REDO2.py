
class Solution:
    def findBall(self, grid:list[list[int]]) -> list[int]:
        
        # Initialise output
        answer = [0]* len(grid[0])
        
        def recursive(row: int, col:int) -> int:
            if row == len(grid):
                    return col
            # Check that the ball is not out of bounds 
            elif row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0:
                return -1
            # The ball is passed the last row, therefore succesfully escaping the grid
          
            
            # If not out of bounds or out of grid, check where the board pushes the ball
            else:
                # If the board pushes the ball to the right
                if grid[row][col] == 1:
                # Check that it does not get push to the wall or outside the grid (invalid)
                # and that it does not get stuck in a "V" pattern
                    if col+1 > len(grid[0])-1 or grid[row][col+1] == -1:
                        return -1
                # The ball is safely pushed to the adjacent right column
                    else:
                        col +=1
                        row +=1
                        return recursive(row, col)
                        

                # If the board pushes the ball to the left
                else:
                # Check that it does not get pushed to the wall or outside the grid (invalid)
                # and that it does not get stuck in a "V" pattern
                    if col-1 < 0 or grid[row][col-1] == 1:
                        return -1
                    else:
                    # The ball is safely pushed to the adjacent left column
                    # Update new row and column
                        col -=1
                        row +=1
                        return recursive(row, col)
                                
            
        
        # Call recursive function for each ball
        for i in range(len(grid[0])):
            res = recursive(0,i)
            answer[i] = res
            
            
        return answer
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]))
    print(sol.findBall([[-1]]))
    print(sol.findBall([[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]))
    print(sol.findBall([[-1,-1]]))

# Time complexity: O(M x N)
# M = number of rows in grid, N = number of columns in grid
    # The for loop drops one ball per column: N balls
    # Each ball makes at most M + 1 recursive calls (one per row, plus the exit check), O(1) work each -> O(M)
    # Total: N x O(M) = O(M x N)

# Space complexity: O(M)
# M = number of rows in grid
    # The call stack holds at most M + 1 frames at once (one per row the ball passes)
    # The output list (N elements) is not counted as additional memory
    
