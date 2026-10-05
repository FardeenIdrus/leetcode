class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        
        # Grid dimensions: M rows, N columns
        row_boundary = len(grid)
        column_boundary = len(grid[0])
        # Land cells already counted as part of an island
        visited_set = set()
        # Number of islands found so far
        num_islands = 0
        
        # DFS: marks a land cell and every land cell connected to it as visited
        # This is how one whole island gets "used up" so it is never counted twice
        def dfs_recursive(row: int, column: int) -> None:
            # Only explore this cell if it is in bounds, not yet visited, and land
            if 0 <= row < row_boundary and 0<= column < column_boundary and (row, column) not in visited_set and grid[row][column]!= "0":
                cell = (row, column)
                visited_set.add(cell)
                # Spread to the 4 neighbours: down, up, left, right
                dfs_recursive(row+1, column)
                dfs_recursive(row-1, column)
                dfs_recursive(row, column -1)
                dfs_recursive(row, column +1)
        
            return
        
        # Check every cell in the grid
        for row in range(row_boundary):
            for column in range(column_boundary):
                cell = (row, column)
                # An unvisited land cell must belong to a new island
                if cell not in visited_set and grid[row][column] == "1":
                    num_islands +=1
                    # Mark the whole island as visited so its other cells are skipped later
                    dfs_recursive(row, column)
        
        return num_islands
    
# Time complexity: O(M x N), where M is the number of rows and N the number of columns
    # A land cell is processed only the first time dfs_recursive reaches it: it is added to visited_set and makes 4 calls
    # Every later call on that cell returns immediately at the "not in visited_set" check, which is O(1)
    # Each cell receives only a constant number of calls (up to 4 from its neighbours, plus the for loop's own check)
    # So total work is proportional to M x N
    
# Space complexity: O(M x N)
    # visited_set: in the worst case every cell is land, so it holds M x N cells
    # Recursion stack: its depth is the number of calls started but not yet finished (the length of the current path of cells)
    # A snake-shaped island can make that path cover all M x N cells
    # num_islands is a single integer: O(1)
    # visited_set and the stack both scale with M x N, so space complexity is O(M x N)
    
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