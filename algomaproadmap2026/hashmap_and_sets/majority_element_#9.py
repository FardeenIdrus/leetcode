from collections import Counter

class Solution: 
    def majorityElement(self, nums: list[int]) -> int:
        
        # Get the minimum number of times a majority element has to be present in nums
        majority = len(nums) /2
        
        # Dictionary storing the count of each element in nums
        ctr = Counter(nums)
        
        # Loop through each dictionary key
        for i in ctr:
            # Access the value at each key and check if its value is greater than majority
            if ctr[i] > majority:
            # If yes, that element is the majority element
                return i
        
    
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([3,2,3]))
    print(sol.majorityElement([2,2,1,1,1,2,2]))
    
# Time complexity: O(n), where n is the total number of elements in nums
    # Counter() has to scan every element in nums to count the frequency of each element - O(n)
    # The dictionary ctr only stores unique elements, so the for loop only iterates through these
    # unique values  - O(K)
    # The "if ctr[i] > majority" is a O(1) look up operation
    # O(n) is always >= O(k), because the number of unique elements in nums can never exceed
    # n (total elements). So O(n) + O(k) simplifies to O(n)
    
# Space complexity: O(k), where k is the number of unique elements in nums
    # Space scales with the number of unique elements in nums