from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        num_islands = 0
        visited_set = set()
        row_boundary = len(grid)
        column_boundary = len(grid[0])
        
        def recursive_dfs(row: int, column: int):

            if (0<= row < row_boundary) and (0<= column < column_boundary) and (row,column) not in visited_set and (grid[row][column] != "0"):
                visited_set.add((row, column))
                recursive_dfs(row+1, column)
                recursive_dfs(row-1, column)
                recursive_dfs(row, column+1)
                recursive_dfs(row, column-1)
        
        
        for row in range(row_boundary):
            for column in range(column_boundary):
                if (row,column) not in visited_set and grid[row][column] != "0":
                    num_islands +=1
                    recursive_dfs(row, column)
        
        return num_islands


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
    
    