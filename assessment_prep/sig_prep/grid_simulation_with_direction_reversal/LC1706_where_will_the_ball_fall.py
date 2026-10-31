
class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        
        res =[0] * len(grid[0])
        

        
        for i in range(len(grid[0])):
            
            row = 0
            col = i
            
            while row!= len(grid) and col!= len(grid[0]):
                
                # Board pushes the ball to the left 
                    # Check that the board in the current cell pushes the ball into a wall
                    # Or that the cell to its immediate left contains a board facing right (V trap)
                if grid[row][col] == -1:
                    col -=1
                    if col <0 or grid[row][col] == 1:
                        col = -1
                        break
                     # If not, the ball succesfully moves to the next row and column
                    else:
                        row += 1
                
                 # Board pushes the ball to the right
                 # Check that the board in the current cell pushes the ball into a wall
                 # Or that the cell to its immediate right contains a board facing left (V trap)
                elif grid[row][col] ==1:
                    col +=1
                    if col >= len(grid[0]) or grid[row][col] == -1:
                        col = -1
                        break
                    else:
                        # If not, the ball succesfully moves to the next row and column
                        row +=1
            
            res[i] = col
                        
                    
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]))