
class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        
        
        # Output list. Pass 1 stores each index's left sum here, pass 2 overwrites it with the final difference
        answer= [0 for _ in nums]
        
        # Running total of the sum of elements to the left of index i
        left_sum = 0
        # Running total of the sum of elements to the right of index i
        right_sum = 0 
        
        # Loop from the second element to the last element
        # Index 0 is skipped: its left sum is 0, which answer[0] already holds
        # nums[i-1] at i= 0 would wrongly wrap around to the last element
        for i in range(1,len(nums)):
            # Compute the sum of elements before index i
            left_sum = nums[i-1] + left_sum
           # Store the left sum of index i in answer[i]
            answer[i] = left_sum
            
        # Loop from the second last index down to 0
        # The last index needs no update: its right sum is 0, so |left sum - 0| equals the left sum already stored in answer
        for i in range(len(nums)-2,-1,-1):
            # Compute the sum of elements to the right of index i
            right_sum = nums[i+1] + right_sum
            
            # answer[i] holds the left sum of index i, and right_sum is the right sum of index i
            # Overwrite answer[i] with |left sum - right sum|, which is the final value for index i
            answer[i] = abs(answer[i] - right_sum)
        
        return answer
    
# Time Complexity: O(n), where n is the number of elements in nums
    # Creating answer: O(n)
    # First for loop: n-1 iterations, O(1) work each, so O(n-1) simplifies to O(n)
    # Second for loop: n-1 iterations, O(1) work each, so O(n-1) simplifies to O(n)
    # Assigning to a list index is O(1) because no elements need shifting
    # The three steps run one after the other, so their costs add: O(n) + O(n) + O(n) = O(n)

# Space Complexity: O(1) when excluding the required output list
    # left_sum and right_sum are constant in size and do not grow with the input nums (their memory size is constant)

if __name__ == "__main__":
    sol = Solution()
    print(sol.leftRightDifference([10,4,8,3]))
    print(sol.leftRightDifference([1]))
    

    
