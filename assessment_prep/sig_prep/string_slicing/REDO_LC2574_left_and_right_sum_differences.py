
class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        
        answer = [0] * len(nums)
        
        if len(nums) == 0:
            answer[0] = 0
            return answer
        
        leftsum = 0
        right_sum = 0
        
        for i in range(1, len(nums)):
            leftsum += nums[i-1]
            answer[i] = leftsum
            
        for i in range(len(nums)-2, -1, -1):
            right_sum += nums[i+1] 
            answer[i] = abs(answer[i] - right_sum)
        
        return answer


if __name__ == "__main__":
    sol = Solution()
    print(sol.leftRightDifference([10,4,8,3]))
    print(sol.leftRightDifference([1]))