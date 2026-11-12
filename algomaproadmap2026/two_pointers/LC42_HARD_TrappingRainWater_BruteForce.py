# Brute Force solution
class Solution:
    def trap(self, height: list[int]) -> int:

        # Main idea: the water above one block = min(tallest block on its left, tallest block on its right) - height of the block
        # If this is negative, the block holds no water, so it counts as 0. The water rises to the shorter of the two walls and spills over it.
        # Add this up over every block.

        # left and right store the tallest block seen so far, excluding the current block we are at.
        # left is found scanning from the left, right is found scanning from the right.
        # For example [0,0,1]: at index 2, the tallest block on its left is 0, and on its right is 0 (nothing is there).
        # At index 0, the tallest block on its right is 1.
        left, right = 0,0
        n = len(height)

        # Two lists with one value per block:
        # max_left[i] is the tallest block to the left of index i, not including i
        # max_right[i] is the tallest block to the right of index i, not including i
        # These are the two numbers the water formula needs for every block. Storing them once here
        # avoids rescanning the left and right of every block, which would be O(n^2)
        max_left = [0] * n
        max_right = [0] * n

        # Variable to store the total trapped water
        total_trapped_water = 0

        # i moves from left to right
        for i in range(n):
            # j moves from right to left (j = -1 is the last block, j = -n is the first block)
            j = -i-1
            # Store the tallest block seen before position i (from the left) and before position j (from the right)
            # This is done BEFORE updating left and right, so the current block is not counted as taller than itself
            max_left[i] = left
            max_right[j] = right

            # Now include the current blocks, so left and right are ready for the next iteration
            left = max(left, height[i])
            right = max(right, height[j])

        # Compute the amount of trapped water above each block
        for i in range(n):
            # pot is the water level above this block: the shorter of its two tallest walls
            pot = min(max_left[i], max_right[i])
            # If the block is taller than the water level (for example index 0, which has no wall on its left),
            # no water sits above it, so we add 0 instead of a negative number
            total_trapped_water += max(0, pot - height[i])

        return total_trapped_water


# Time complexity: O(n), where n is the number of elements in height
    # The first for loop runs n times (visits each element once), and fills both lists in the same pass -> O(n)
    # Each iteration does O(1) work
    # O(n) * O(1) = O(n)
    # The second for loop also runs n times doing O(1) work in each iteration. O(n) * O(1) = O(n)
    # The loops run one after the other, so costs add: O(n) + O(n) = O(2n), which simplifies to O(n)

# Space complexity: O(n), where n is the number of elements in height
    # max_left and max_right store n elements each. O(2n) simplifies to O(n)
    # left, right, n, total_trapped_water, i, j and pot take constant space in memory -> O(1)
    # Total = O(n) + O(1) = O(n)