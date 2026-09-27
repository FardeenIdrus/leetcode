
class Solution:
    def productExceptSelf(self, nums: list[int]) -> int:
        
        prefix = 1
        result = [1] * len(nums)
        suffix = 1
        
        for i in range(1,len(nums)):
            result[i] = prefix * nums[i-1]
            prefix = prefix * nums[i-1] 
            
        for j in range(len(nums)-2,-1, -1):
            
            result[j] = result[j] * suffix * nums[j+1] 
            suffix = suffix * nums[j+1]      
        
    
        
        return result



if __name__ == "__main__":
    sol = Solution()
    print(sol.productExceptSelf([1,2,3,4]))
    print(sol.productExceptSelf([-1, 1, 0,-3,3 ]))

# Time complexity : O(n), where n is the number of elements in the input array
    # 2 for loops
    # First loop iterates through n-1 elements
    # Second for loop iterates through n-1 elements
    # O(2(n-1)) = O(2n-2) which is dominated by O(n)
    # Each element is visited only once in each pass

# Space complexity: O(1) if excluding the output data structure. Variables prefix and suffix are constant in size
# and dont grow with the size of input nums
# If including the output data structure - O(n) where n is the number of elements in the nums arrray 