
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        def recursive_dfs(row: int, col: int):
            
            if 0<= row < m and 0<= col < n and grid[row][col] ==1:
                
                grid[row][col] = 0
                return 1+ recursive_dfs(row+1, col) + recursive_dfs(row-1, col) + recursive_dfs(row, col-1) + recursive_dfs(row, col+1)
        
            return 0 
        
        max_area = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    max_area = max(max_area, recursive_dfs(row,col))
                    
        
        return max_area
    


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
    print(sol.maxAreaOfIsland([[0,0,0,0,0,0,0,0]]))