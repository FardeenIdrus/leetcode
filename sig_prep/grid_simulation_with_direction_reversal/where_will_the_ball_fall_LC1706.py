class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        # One slot per ball (1 is a placeholder, overwritten below)
        answer = [1] * len(grid[0])

        def dfs_recursive(row: int, col: int) -> int:
            # Past the last row: the ball fell out, return its column
            if row == len(grid):
                return col

            # Board is 1: the ball is pushed one column right
            elif grid[row][col] == 1:
                col += 1
                # Stuck if it hits the right wall or the next board slopes left (a V)
                # Wall check goes first so we never read outside the grid
                if col == len(grid[0]) or grid[row][col] == -1:
                    return -1

            # Board is -1: the ball is pushed one column left
            elif grid[row][col] == -1:
                col -= 1
                # Stuck if it hits the left wall or the next board slopes right (a V)
                # Wall check goes first: grid[row][-1] would silently read the last column
                if col < 0 or grid[row][col] == 1:
                    return -1

            # Not stuck: move down one row and pass the result back up
            return dfs_recursive(row + 1, col)

        # Drop one ball into each column, starting at row 0
        for i in range(len(grid[0])):
            answer[i] = dfs_recursive(0, i)
        return answer

# Time complexity: O(n * m), where n is the number of columns and m is the number of rows
    # Creating answer: n slots -> O(n)
    # For loop: n iterations, one per ball
    # Each ball: at most m recursive calls (one per row), O(1) work each -> O(m)
    # All balls: n * O(m) = O(n * m)
    # The steps run one after the other, so their costs add: O(n) + O(n * m) = O(n * m)

# Space complexity: O(m)
    # answer: n slots, but it is the return value so it is not counted
    # Recursion stack: at most m + 1 calls at once (one per row, plus the call that returns) -> O(m)
    # i, row and col are single integers -> O(1)
    # Total: O(m)


if __name__ == "__main__":
    sol = Solution()
    print(sol.findBall([[1, 1, 1, -1, -1], [1, 1, 1, -1, -1], [-1, -1, -1, 1, 1], [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]]))  # [1, -1, -1, -1, -1]
    print(sol.findBall([[-1]]))  # [-1]
    print(sol.findBall([[1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1], [1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1]]))  # [0, 1, 2, 3, 4, -1]