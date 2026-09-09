from typing import List
from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        seen_dict = defaultdict(int)
        for i in range(len(nums)):
            if seen_dict[nums[i]]:
                return True
            else:
                seen_dict[nums[i]] =1
                
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.hasDuplicate([1,3,2]))