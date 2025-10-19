from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]
        for i in nums:
            if abs(i) < abs(closest):
                closest = i
        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest
        
# Time Complexity: O(n²) - we loop O(n) and do an O(n) lookup with "in nums"
# Space Complexity: O(1) - only using a few variables, no extra data structures

if __name__ == "__main__":
    solution = Solution()
    print(solution.findClosestNumber(nums = [-4,-2,1,4,8]))