from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result_list = [1] *len(nums)
    
        running_suffix = 1
        for i in range(1,len(nums)):
           result_list[i] = result_list[i-1]* nums[i-1]
           
        for i in range(len(nums)-1,-1,-1):
            result_list[i] = running_suffix * result_list[i] 
            running_suffix = running_suffix * nums[i]  
    
        return result_list

if __name__ == "__main__":
    sol = Solution()
    print(sol.productExceptSelf([2,3,4,5]))
    
#Time complexity : O(n) -> only visit each element in the list once
# Space complexity: O(1) -> one extra variable that remains constant sized 