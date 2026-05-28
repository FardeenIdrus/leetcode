from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result_list = [1] *len(nums)
        
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if j!=i:
                    product *= nums[j]
            
            result_list[i] = product
        return result_list
        



if __name__ == "__main__":
    sol = Solution()
    print(sol.productExceptSelf([1,2,3,4]))
    print(sol.productExceptSelf([-1,1,0,-3,3]))
    print(sol.productExceptSelf([2]))