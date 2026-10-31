from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        
        
        counter = 0
                
        
        for i in range(len(nums)):
            
            running_sum = 0 
            for j in range(i, len(nums)):
                running_sum += nums[j]
                if running_sum == k:
                    counter +=1

        return counter 


# Time complexity: O(n^2), where n is the number of integers in nums
    # The outer for loop runs n times, once per start index i
    # The inner for loop runs from index i to the last index, so it runs n - i times:
    # n times when i = 0, n - 1 times when i = 1, down to 1 time when i = n - 1
    # Total iterations: n + (n - 1) + ... + 1 = n(n + 1) / 2, which is n^2 / 2 + n / 2
    # Dropping the constant and the lower-order term gives O(n^2)
    # Each iteration does O(1) work, so the total time is O(n^2)
    
# Space complexity: O(1)
    # i and j are integers and are constant in size -> O(1)
    # The variables counter and running_sum are constant in size -> O(1)
    # O(1) + O(1) + O(1) + O(1) simplifies to O(1)
    # No extra data structure is used and the amount of memory used is constant 



if __name__ == "__main__":
    sol = Solution()
    print (sol.subarraySum([1,1,1],2))
    print(sol.subarraySum([1,2,3],3))
    print(sol.subarraySum([1,2,3,0,5],3))
