from collections import defaultdict
from typing import List

# Function take takes a list of integers and an integer, and returns the count of that integer in the list

class Solution:
    def countElemets(self, nums: List[int], i: int) -> List[int]:
        dictionary = defaultdict(int)
        for j in range(len(nums)):
            dictionary[nums[j]] += 1

        return dictionary[i]

if __name__ == "__main__":
    sol = Solution()
    print(sol.countElemets([1,1,1,2,2,3],1))
    