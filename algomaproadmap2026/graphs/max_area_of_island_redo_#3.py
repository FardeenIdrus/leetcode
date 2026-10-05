
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        
        visited_set = set()
        
        row_boundary = len(grid)
        column_boundary = len(grid[0])
        max_area = 0
        
        
        def dfs_recursive(row: int, column: int): 
            
            # Only count this cell if it's in bounds, unvisited and is a land cell
            if 0<= row < row_boundary and 0<= column < column_boundary and (row, column) not in visited_set and grid[row][column] ==1:
                visited_set.add((row, column))                
            
                # 1 for this cell, plus the island size found through each of the 4 neighbours
                return 1+dfs_recursive(row-1, column) + dfs_recursive(row+1, column)+ dfs_recursive(row, column-1)+ dfs_recursive(row, column+1)
            
            # Out of bounds, water, or already visited: adds nothing to the area
            return 0
        
        for row in range(row_boundary):
            for column in range(column_boundary):
                if (row, column) not in visited_set and grid[row][column] == 1:
                    # Call dfs_recursive once and save the result. A second call on the same cell would return 0, because the island is already visited
                    island_size = dfs_recursive(row, column)
                    max_area = max(max_area, island_size)
                    
        
        
        
        return max_area
    
'''
Time complexity: O(M x N), where M is the number of rows in grid, and N the number of columns in grid
    - The for loop checks every cell once: M x N checks
    - A land cell is processed only the first time dfs_recursive reaches it: it is added to visited_set and makes 4 calls
    - Every later call on that cell returns 0 immediately, because the cell is already in visited_set
    - Islands never overlap, so across all islands, every cell is processed at most once
    - Total dfs_recursive calls: 4 per land cell, plus 1 per island (made by the for loop). Each call does constant work
    - The loop checks and the calls are both at most a constant multiple of M x N, so the total is O(M x N)

Space complexity: O(M x N)
    - visited_set: worst case the whole grid is land, so it holds M x N coordinates
    - Recursion stack: its depth is the number of calls started but not yet finished (the length of the current path of cells).
      A snake-shaped island can make that path cover every cell, so the depth can reach M x N
    - max_area and island_size are single integers: O(1)
    - Total: O(M x N) + O(M x N) + O(1) = O(M x N)
'''



if __name__ == "__main__":
    sol = Solution()
    print(sol.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
    print(sol.maxAreaOfIsland([[0,0,0,0,0,0,0,0]]))
    
