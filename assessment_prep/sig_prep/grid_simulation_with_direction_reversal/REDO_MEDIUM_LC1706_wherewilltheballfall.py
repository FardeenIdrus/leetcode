
class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:

        
        res = [None] * len(grid[0])

        def dfs_recursive(row: int, col:int):
            
            # ball current row = outside the bottom of the box - return col
            if row == len(grid):
                return col


            # If the board in this cell pushes the ball to the right, check that the cell directly to its right does not have a board pushing it left (V trap)
            # Or that it is already in the last column and pushing it to the right gets it stuck
            # on the wall
        
            if grid[row][col] == 1:
                if col+1 == len(grid[0]) or  grid[row][col+1] == -1:
                    return -1
                else: 
            # If there is no opposite facing board in the immediate cell to its right
            # the ball successfully falls down to row+1, col+1
                    return dfs_recursive(row+1, col+1)

            # If the board in this cell pushes the ball to the left, check that the cell directly to its left does not have a board pushing it right (V trap)
            # Or that it is already on the first column and pushing it to the left gets it stuck on the wall
            elif grid[row][col] == -1:
                if col-1 <0 or grid[row][col-1] == 1:
                    return -1 
                else:
                    return dfs_recursive(row+1, col - 1)
                    
                    
        for ball in range(len(grid[0])):

            res[ball] = dfs_recursive(0, ball)
            
        

        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]))