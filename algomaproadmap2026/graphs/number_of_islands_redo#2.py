
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        
        # Set row and column boundaries 
        row_boundary = len(grid)
        column_boundary = len(grid[0])
        # Initialise a set to track the visited cells 
        visited_set = set()
        # Initialise variable to track number of visited islands
        num_islands = 0
        
        # DFS Recursive function to traverse through neighbouring "1" cells that are part of the individual islands
        def dfs_recursive(row: int, column: int) -> None:
            # For each neighbouring cell - check that it is within the grid boundary, has not been visited, and is not a water cell
            if 0 <= row < row_boundary and 0<= column < column_boundary and (row, column) not in visited_set and grid[row][column]!= "0":
                cell = (row, column)
                # Add the current cell coordinates to the set of visited cells
                visited_set.add(cell)
                # Call the recursive function on neighbouring cells to check if they are also apart of the island
                dfs_recursive(row+1, column)
                dfs_recursive(row-1, column)
                dfs_recursive(row, column -1)
                dfs_recursive(row, column +1)
        
            return
        
        # Loop through each cell in the grid
        for row in range(row_boundary):
            for column in range(column_boundary):
                cell = (row, column)
                # If the cell has not been visited as is a new island cell that has not been visited
                if cell not in visited_set and grid[row][column] == "1":
                    # It is a new island - increment the number of islands in the grid
                    num_islands +=1
                    # Call the recursive function on this cell to check whether the neighbouring cells are also a part of this island
                    # This ensures we are not counting connected "1" cells as separate islands
                    dfs_recursive(row, column)
        
        return num_islands
    
# Time complexity: O(M X N) where M is the number of rows and N the number of columns in grid
    # Each cell can be checked a constant number of times - up to 5 times - once by the for loop, and up to 4 more times as a neighbour of adjacent cells 
    # calling dfs_recursive
    # A cell is only explored fully (added to visited_set or recursed into by adjacent cells calling dfs_recursive) the first timed it is reached
    # Subsequent checks on that cell is O(1) because of the "not in visited_set" check which is a look-up operation - O(1)
    # Since each cell can be checked at most a small constant number of times, the time complexity stays proportional to O(M X N)
    
    
# Space complexity: 
    # In the worst case, every cell is an island, therefore visited_cell will hold up to O(M x N) cells
    # num_islands is constant in size and does not grow with the input - O(1)
    # In the worst case, each cell in the grid is a land cell, and in this case, there will be M x N calls waiting on the recursive stack
    # Both parts scale with M x N, so the space time complexity is O(M x N)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))
    
    print(sol.numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))
    