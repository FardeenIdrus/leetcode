from collections import defaultdict
import itertools

class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:

        # Key = row + column. Cells with the same sum lie on the same diagonal.
        # Value = list of the numbers on that diagonal.
        diagonal_dict = defaultdict(list)

        # Scanning row by row, left to right, adds each diagonal's numbers
        # from top-right down to bottom-left. Diagonals are created in order 0, 1, 2, ...
        for row in range(len(mat)):
            for column in range(len(mat[0])):
                cell_sum = row + column
                diagonal_dict[cell_sum].append(mat[row][column])

        # Even diagonals must go bottom-left to top-right, the opposite of how we stored them.
        # reverse() changes the list inside the dictionary directly, so nothing needs putting back.
        for key in diagonal_dict:
            if key % 2 == 0:
                value = diagonal_dict[key]
                value.reverse()

        # Join all diagonals in key order into one list
        diagonal_list = list(itertools.chain.from_iterable(diagonal_dict.values()))

        return diagonal_list

# Time complexity: O(m * n), where m is the number of rows and n the number of columns in mat
    # Nested for loops: m * n cells, O(1) append each -> O(m * n)
    # Second for loop: m + n - 1 keys, and the reversed lists hold at most m * n values in total -> O(m * n)
    # chain + list(): copies m * n values into the output -> O(m * n)
    # The steps run one after the other, so their costs add: O(m * n) + O(m * n) + O(m * n) = O(m * n)

# Space complexity: O(m * n)
    # diagonal_dict: m + n - 1 lists holding m * n values in total -> O(m * n)
    # diagonal_list: m * n values, but it is the return value so it is not counted
    # row, column, cell_sum, key and value are single integers or references to existing lists -> O(1)
    # Total: O(m * n)


if __name__ == "__main__":
    sol = Solution()
    print(sol.findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # [1, 2, 4, 7, 5, 3, 6, 8, 9]
    print(sol.findDiagonalOrder([[1, 2], [3, 4]]))  # [1, 2, 3, 4]
        