from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        
        closest_number_to_zero = nums[0]
        
        for i in range(1, len(nums)):
            if abs(nums[i]) < abs(closest_number_to_zero):
                closest_number_to_zero = nums[i]
            elif abs(nums[i]) == abs(closest_number_to_zero):
                closest_number_to_zero = max(nums[i], closest_number_to_zero)

        return closest_number_to_zero
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.findClosestNumber([-4,-2,1,4,8]))
    print(sol.findClosestNumber([-2,-1,1]))
    print(sol.findClosestNumber([-100000,-100000]))
    
# Time complexity : O(n) -> Where n is the number of elements in the input list
# We iterate through each element in the input List once

#Space complexity: O(1) -> Extra memory used is the variable closest_number_to_zero which does not grow with input size

    


        