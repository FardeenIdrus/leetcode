from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result_list = [1]*len(nums)
        running_suffix= 1
        
        for i in range(1,len(nums)):
            result_list[i] = nums[i-1] * result_list[i-1]
            
        for i in range(len(nums)-1,-1,-1):
            result_list[i] = result_list[i] * running_suffix
            running_suffix = running_suffix * nums[i]
            print(running_suffix)
            
        return result_list

    
if __name__ == "__main__":
    sol = Solution()
    print(sol.productExceptSelf([1,2,3,4]))
    #print(sol.productExceptSelf([-1,1,0,-3,3]))
    

# Time complexity: O(n): Two sequential O(n) passes gives O(2n) which simplifies to O(n)

# Space complexity: O(1): Only additional memory used is a single variable which stores an integer

    
    
    