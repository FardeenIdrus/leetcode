from typing import List 
class Solution:
    def hasDuplicate(self, nums:List[int]) -> bool:
        thisset = {""}
        for i in range (len(nums)):
            if nums[i] not in thisset:
                thisset.add(nums[i])
            else:
                return True
        return False
    
    
#Time complexity: 
if __name__ == "__main__":
    sol = Solution()
    num_array = [1,2,3,3]
    print(sol.hasDuplicate(num_array))
    
    
    