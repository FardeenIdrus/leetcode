from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        running_product = 1
        result_list = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1]*nums[i-1]

        for i in range(len(nums)-1, -1, -1):
            suffix[i] = suffix[i] * running_product
            running_product = running_product * nums[i]
            
        
        for i in range(len(nums)):
            result_list[i] = prefix[i] * suffix[i]
        
        return result_list





if __name__ == "__main__":
    sol = Solution()
    print(sol.productExceptSelf([1,2,3,4]))
    print(sol.productExceptSelf([-1,1,0,-3,3]))