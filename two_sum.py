
from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target:int) -> List[int]:
       hash_map = {}
       #set Key as the nums[i], and value as i
       for i in range(len(nums)):  
           needed = target - nums[i]
           if needed in hash_map:
               return [hash_map[needed], i]
           else:
               
                hash_map[nums[i]] = i

if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([1,2,3,4,5],9))
           
        