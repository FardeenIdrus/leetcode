from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        
        # Initialise to infinity so the first real element always replaces it
        closest_to_zero = float("inf")
        
        #Loop through each element in the array
        for i in range(len(nums)):
        # Take absolute value of the element being compared to closest_to_zero because -x and x have the same distance to zero
        # if the element 
            if abs(nums[i]) < abs(closest_to_zero):
                closest_to_zero = nums[i]
                
        # If both elements have the same distance to zero, take the larger element
            elif abs(nums[i]) == abs(closest_to_zero):
                closest_to_zero = max((nums[i]), closest_to_zero)
                

        return closest_to_zero
    
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.findClosestNumber([-4,-2,1,4,8]))
    print(sol.findClosestNumber([2,-1,1]))

# Time complexity = O(n) where n is the number of elements in the input list. Iterate through each element one at a time.
# Space complexity = O(1). The variable closest_to_zero does not grow with the input array