from collections import defaultdict

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Maps a number we've already seen to its index
        num_dict = {}

        for i in range(len(nums)):
            # The number that would complete the pair with nums[i]
            remainder = target - nums[i]

            # If we've already seen that number, we've found the pair
            if remainder in num_dict:
                return [num_dict[remainder], i]

            # Otherwise, record this number so later numbers can find it
            num_dict[nums[i]] = i

        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))
    print(sol.twoSum([3, 2, 4], 6))
    print(sol.twoSum([3, 3], 6))