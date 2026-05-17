from typing import List

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         prefix = [1] * len(nums)
#         suffix = [1] * len(nums)
#         result_list = [1] * len(nums)
#         for i in range(1,len(nums)):
#             prefix[i] = prefix[i-1] *nums[i-1]

#         for i in range(len(nums)-2,-1,-1):
#             suffix[i] = suffix[i+1] * nums[i+1]
            
#         for i in range(len(nums)):
#             result_list[i] = suffix[i] *prefix[i]
#         return result_list

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        running_suffix =1 
        result_list = [1] * len(nums)
        for i in range(1,len(nums)):
            result_list[i] = result_list[i-1] *nums[i-1]

        for i in range(len(nums)-1,-1,-1):
            result_list[i] = running_suffix * result_list[i]
            running_suffix = running_suffix * nums[i]
            
        return result_list

if __name__ == "__main__":
    sol = Solution()
    print(sol.productExceptSelf([1,2,4,6]))
