class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        # low and high are the first and last indexes where the target could still be
        low = 0
        high = len(nums) - 1

        while low <= high:
            # mid is the index in the middle of the current range
            mid = (high + low) // 2

            if nums[mid] < target:
                # Middle is too small, so the target is to the right: drop the left half
                low = mid + 1
            elif nums[mid] > target:
                # Middle is too big, so the target is to the left: drop the right half
                high = mid - 1
            elif nums[mid] == target:
                # Found it (works because the numbers are distinct)
                return mid

        # Not found: the loop ended with low > high, and low is the index where
        # the target would be inserted to keep the list sorted
        return low

# Time complexity: O(log n), where n is the number of integers in nums
    # Setting low and high: O(1)
    # While loop: each iteration halves the range between low and high, so at most log2(n) + 1 iterations, O(1) work each -> O(log n)
    # The steps run one after the other, so their costs add: O(1) + O(log n) = O(log n)

# Space complexity: O(1)
    # low, high and mid are single integers -> O(1)
    # No extra list is created
    # Total: O(1)


if __name__ == "__main__":
    sol = Solution()
    print(sol.searchInsert([1, 3, 5, 6], 5))  # 2
    print(sol.searchInsert([1, 3, 5, 6], 2))  # 1
    print(sol.searchInsert([1, 3, 5, 6], 7))  # 4
    print(sol.searchInsert([10, 20, 30, 40, 50], 25))  # 2