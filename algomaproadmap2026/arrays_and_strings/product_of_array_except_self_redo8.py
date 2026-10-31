

class Solution:
    def productExceptSelf(self, nums:list[int]) -> list[int]:
        
        answer = [1] * len(nums)
        prefix = 1
        suffix = 1
        
        for i in range(1,len(nums)):
            prefix = prefix * nums[i-1]
            answer[i] = prefix
            
        for i in range(len(nums)-2, -1, -1):
            suffix = suffix * nums[i+1]
            answer[i] = suffix * answer[i]
            
        
        return answer
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.productExceptSelf([1,2,3,4]))
    print(sol.productExceptSelf([-1,1,0,-3,3]))

# Time Complexity: O(n), where n is the number of elements in nums
    # The first for loop iterates through n-1 elements doing O(1) work 
    # The second for loop iterates through n-1 elements doing O(1) work 

# Space Complexity: O(1) 
    # Variables prefix and suffix are integers, which are constant in size
    # No extra data structures are used other than the output list