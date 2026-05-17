from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result_list = [1] *len(nums)
    
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j!=i:
                    result_list[i] = result_list[i] *nums[j]
                
    
        return result_list

if __name__ == "__main__":
    sol = Solution()
    print(sol.productExceptSelf([2,3,4,5]))