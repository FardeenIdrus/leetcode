
from typing import List
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        
        closest_num_to_zero = nums[0]
        for i in range(1,len(nums)):
            if abs(nums[i]) < abs(closest_num_to_zero):
                closest_num_to_zero = nums[i]
            elif abs(nums[i]) == abs(closest_num_to_zero):
                closest_num_to_zero = max(closest_num_to_zero, nums[i])
        
        return closest_num_to_zero
        
        
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.findClosestNumber([-1,1,3,-2]))
    
    #expect to return 1
    
    
# Time complexity: O(n) - Accessing each element in the input list once
# Space compplexity: O(1) - Variable closest__num_to_zero is a integer 