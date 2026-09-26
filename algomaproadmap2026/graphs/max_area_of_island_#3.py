from collections import defaultdict
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        
        
        visited_set = set()
        row_boundary = len(grid)
        column_boundary = len(grid[0])
        max_area =0 
        island_size = 0
        def recursive_dfs(row: int, col: int):
       

            if 0 <= row < row_boundary and 0 <= col < column_boundary and (row,col) not in visited_set and grid[row][col] ==1:
            
                visited_set.add((row, col))
                
                right = recursive_dfs(row, col + 1)
                left = recursive_dfs(row, col -1)
                up = recursive_dfs(row -1, col)
                down = recursive_dfs(row+ 1,col)
                
                return 1+ right + left +up + down
        
            return 0 
        
        
        for row in range(row_boundary):
            for column in range(column_boundary):
                if (row,column) not in visited_set and grid[row][column] == 1:
                    island_size = recursive_dfs(row, column)
                    if island_size > max_area:
                        max_area = island_size                    

        
        
        return max_area


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
    print(sol.maxAreaOfIsland([[0,0,0,0,0,0,0,0]]))
    
    
# Time complexity: O(mx n), where m is the number of rows and n is the number of columns.
# Each cell is checked a constant number of times (once from the main loop, up to 4 more
# times as a neighbour's check) - a fixed multiplier, not something that grows with grid size
# so total work stays proportional to m x n

# Space complexity: O(m x n). visited_set can hold every cell in the worst case (all land).
# Separately, the recursion call stack can go m x n calls deep in the worse case (one island
# spanning the whole grid) before any calls return. Both scale with m x n. 