from typing import List

class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # Initialise island counter
        islands = 0
        
        # Set row and column boundaries 
        row_boundary = len(grid)
        column_boundary = len(grid[0])
        
        # Initialise a set to track visited cells 
        visited_set= set()

        # Recursive dfs function to explore all unexplored neighbouring cells 
        def recursive_dfs(row: int, col: int):
        
        # Check that the neighbouring cell is not out of the grid (index out of range error),
        # is not water (you dont want to explore the water cell's neighbour), and has not already been visited
            if (0<= row < row_boundary and 0<=col < column_boundary) and (grid[row][col] != "0") and ( (row,col) not in visited_set):
                visited_set.add((row, col))
                # Check neighbour vertically below
                recursive_dfs(row+1, col)
                # Chek neighbour vertically above
                recursive_dfs(row-1, col)
                # Check neighbour horizontally to the left 
                recursive_dfs(row, col-1)               
                # Check neighbour horizontally to the right
                recursive_dfs(row, col+1)
                
                        
            
        # Loop through each cell in the grid 
        for row in range(row_boundary):
            for column in range(column_boundary):
                # If the cell is an island and has not been visited, increment island counter (start of new island)
                if grid[row][column] == "1" and (row,column) not in visited_set: 
                    islands +=1
                # Call recursive function to explore all of its connected cells (neighbours) so that the connected
                # "1's" are counted as a single island
                    recursive_dfs(row, column)
                    
        
    
        return islands
    
# Time complexity: O(M x N), where M is the number of rows and N is the number of columns.
# The main loop visits every cell once. recursive_dfs only runs its body on a cell the
# first time that cell is reached, because the visited check blocks every later call on
# that same cell. So across the whole program, each cell is fully processed exactly once,
# giving O(M x N) total work.

# Space complexity: O(M x N).
# 1) visited_set: in the worst case every cell is land, so all M x N cells get stored in it.
# 2) Call stack: recursive_dfs calls itself once per cell before returning. In the worst
#    case, every land cell connects to the next in a single unbroken chain, so up to
#    M x N calls can be waiting on the call stack at the same time before any of them return.
# Both parts scale with M x N, so the total space complexity is O(M x N).
    


if __name__ == "__main__":
    sol = Solution()
    print(sol.numIslands([
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]))
    print(sol.numIslands([
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]))