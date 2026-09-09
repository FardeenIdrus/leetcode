from collections import defaultdict
from typing import List
class Solution:
    def twoSum(self, nums:List[int], target:int)-> List[int]:
        remainderDict = defaultdict(int)
        
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in remainderDict:
                return [remainderDict[remainder],i]
            else:
                remainderDict[nums[i]] = i
                
        return False
        
        #Brute force approach 
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([1,2,3,4], 3))



#print((lambda x,y : x*y) (25, 65))