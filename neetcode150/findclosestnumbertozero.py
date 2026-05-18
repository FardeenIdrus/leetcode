
from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        distance_to_zero = float("inf")
        
        for i in range(len(nums)):
            if abs(nums[i]-0) < distance_to_zero:
                distance_to_zero = abs(nums[i]-0)
                largest_number_closest_to_zero = nums[i]
                
            elif abs(nums[i]-0) == distance_to_zero:
                if nums[i] > largest_number_closest_to_zero:
                    largest_number_closest_to_zero = nums[i]
           
            
        return largest_number_closest_to_zero


if __name__ == "__main__":
    sol = Solution()
    # print(sol.findClosestNumber([float("-inf"),1,-1]))
    print(sol.findClosestNumber([-4,-2,1,4,8]))
    print(sol.findClosestNumber([2,-1,1]))
    print(sol.findClosestNumber([-1,1]))
    print(sol.findClosestNumber([5]))


    
# Time complexity: O(n): Only accessing each item in the input list once

# Space complexity: O(1)
# Only extra memory used is distance_to_zero which is an integer -> so constant O(1)