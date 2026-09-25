
from collections import defaultdict
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        num_dict = defaultdict(int)
        
        for i in range(len(nums)):
            num_dict[nums[i]] = i
        
        for j in range(len(nums)):
            remainder = target- nums[j]
            if remainder in num_dict and num_dict[remainder] != j:
                return [j, num_dict[remainder]]
                

            
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2,7,11,15],9))
    print(sol.twoSum([3,2,4], 6))
    print(sol.twoSum([3,3],6 ))
    
# Time complexity: O(n), where n is the number of integers in nums.
# First loop: O(n) - visits every integer once, storing it as a key with its index as the value
# (if a value repeats, only its LAST index survives, since each assignment overwrites the last).
# Second loop: O(n) - visits every integer again; each dictionary lookup (remainder in num_dict)
# and access (num_dict[remainder]) is O(1) average, since dictionaries are hash-based.
# Total: O(n) + O(n) = O(n).

# Space complexity: O(n), where n is the number of UNIQUE integers in nums -
# num_dict stores at most one entry per unique value (duplicates overwrite, not add new entries).
# remainder is a single O(1) variable and doesn't affect this.
