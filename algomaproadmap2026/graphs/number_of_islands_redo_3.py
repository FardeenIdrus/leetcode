from typing import List
from collections import defaultdict

class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        adjacency_list = defaultdict(list)
        
        visited_set = set()
        number_of_islands = 0 
        
        def dfs_recursive(row: int, col:int):
        
            
            if 0<= row < len(grid) and 0<= col < len(grid[0]) and grid[row][col] == "1" and (row,col) not in visited_set:
                    cell = (row, col)
                    visited_set.add(cell)
                    
                    dfs_recursive(row-1, col)
                    dfs_recursive(row+1, col)
                    dfs_recursive(row, col-1)
                    dfs_recursive(row, col+1)
            

            
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                cell = (row, column)
                if cell not in visited_set and grid[row][column] == "1":
                    number_of_islands +=1
                    dfs_recursive(row, column)
        
        
        return number_of_islands
    


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
  ["0","0","0","1","1"]]
))

# Time complexity:

# Space Complexity: 