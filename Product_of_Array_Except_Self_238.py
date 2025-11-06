from typing import List
class Solution:
    def productExceptSelf(self, nums:List[int]) -> List[int]:
        
        product_right = 1
        answer = [1]
        for i in range(1,len(nums)):
            answer.append(answer[-1]*nums[i-1])
        for i in range(len(nums)-1,-1,-1):
            answer[i] = answer[i] *product_right
            product_right *= nums[i]
            
        
        return answer

        
if __name__ == "__main__":
    solution = Solution()
    print(solution.productExceptSelf([1,2,3,4]))
    