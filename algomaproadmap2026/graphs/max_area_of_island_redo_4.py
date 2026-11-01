
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        
        max_area = 0
        # Set storing tuples of visited island cells
        # Used to make sure that visited island cells are not double counted and visited again 
        visited_island_cells = set()
        
        def dfs_recursive(row: int, col: int) -> int:
            
            # Check that the cell being checked is within the valid boundary of the grid and that it has not already been visited
            # and that it is an island cell (1)
            if 0<= row < len(grid) and 0<= col < len(grid[0]) and grid[row][col] == 1 and (row, col) not in visited_island_cells:
                # If all these checks pass - it is an unvisited island cell, so add the cell coordinates to the set
                visited_island_cells.add((row, col))
            
                # Call the recursive function on the neighbouring cells 
                left = dfs_recursive(row, col-1)
                right = dfs_recursive(row, col+1)
                up = dfs_recursive(row-1, col)
                down = dfs_recursive(row+1, col)
                
                # 1+ ... to increment the count (area of the island)
                return 1+left+right+up+down 
            return 0 
                
        # Iterate through each cell on the grid 
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                # Convert the cell's coordinate into a tuple since set can only store immutable elements
                cell = (row, column)
                # Start of a new island
                if cell not in visited_island_cells and grid[row][column] == 1:
                    max_area = max(max_area, dfs_recursive(row, column))
        
        return max_area
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
    print(sol.maxAreaOfIsland([[0,0,0,0,0,0,0,0]]))
    
# Time Complexity: O(m x n), where m is the number of rows in grid and n the number of columns in grid
    # The for loop iterates through each cell in grid -> O(m x n)
    # A land cell is processed only the first time dfs_recursive reaches it: it is added to visited_set
    # and makes 4 calls.
    # Every later call on that cell returns 0 immediately, because the cell is already in visited_set
    # Islands never overlap, so across all islands, every cell is processed at most once
    # Total dfs_recursive calls: 4 per land cell, plus 1 per island (made by the for loop). Each call does
    # constant work
    # The loop checks and the calls are at most a constant multiple of M x N, so the total is O(M x N)
    

# Space Complexity: O(m x n), where m is the number of rows in grid and n is the number of column is grid
    # In the worst case, every cell in the grid is 1, so visited_island_cells holds M x N tuples
    # Recursion stack: its depth is the number of calls started but not yet finished (the length
    # of the current path of cells)
    # A snake shaped island can make that path cover every cell, so the depth can reach M x N
    # max_area is a single integer : O(1)
    # Total : O(M x N) + O(M x N) + O(1) = O(M x N)