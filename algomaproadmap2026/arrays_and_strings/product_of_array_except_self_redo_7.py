
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        suffix = 1
        prefix = 1
        result = [1 for _ in range(len(nums))]
        
        for i in range(1,len(nums)):
            result[i] = prefix * nums[i-1]
            prefix = prefix * nums[i-1]
        
        for i in range(len(nums)-2,-1,-1):
            result[i] = result[i] * nums[i+1] * suffix
            suffix = suffix * nums[i+1]        
        
        
        return result
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.productExceptSelf([1,2,3,4]))
    print(sol.productExceptSelf([-1,1,0,-3,3]))
    
    
# Time complexity : O(n), where n is the number of elements in the input array
    # 2 for loops -> First for loop, loops through n-1 elements, Second for loop, through n-1 elements
    # O(2n-2) -> which simplifies to O(n)
    # Each element gets visited once in each pass
    
# Space complexity : O(1) when excluding the return structure
# Suffix, and prefix are constant in size and do not grow with the size of the input array. If including the
# output - the space complexity is O(n) where n is the number of elements in the input array,
# as the output has to store the product of each element except itself
