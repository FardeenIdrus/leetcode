
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        # Running product of every element seen so far to the left of the current index
        prefix = 1
        
        # Running product of every element seen so far to the right of th ecurrent index
        suffix  = 1    
        
        # Output array, initialised to 1 so untouched positions (e.g. index 0's prefix contribution) are a no-op)
        product = [1 for _ in range(len(nums))]
        
        # Forward pass: fill product[i] with the prefix contribution (product of everything before index i)
        for i in range(1, len(nums)):
            product[i] = nums[i-1] * prefix
    # Update prefix by multiplying in nums[i-1], so it now holds the product of everything up to and including index i-1
            prefix = nums[i-1] * prefix
        
         # Backward pass: multiply in the suffix contribution (product of everything after index i)
        # Runs down to -1 (exclusive), so index 0 is included and gets its suffix multiplied in here too
        for i in range(len(nums)-2, -1, - 1):
            product[i] = product[i] * nums[i+1] * suffix
    # Update suffix by multiplying in nums[i+1], so it now holds the product of everything from index i+1 onward
            suffix = nums[i+1] * suffix 


        return product
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.productExceptSelf([1,2,3,4]))
    print(sol.productExceptSelf([-1,1,0,-3,3]))
    
# Time complexity: O(n) -> two separate loops, each visiting every element once (one for the prefix pass,
# one for the suffix pass) -> O(2n), which simplifies to O(n). n is the number of elements in the input array

# Space complexity: O(1) -> if excluding the output array - prefix and suffix are constants that do not grow with the
# input size. If including the output array -> O(n), where n is the number of elements in each array, as the output 
# has to have the product element for each element in the input array 