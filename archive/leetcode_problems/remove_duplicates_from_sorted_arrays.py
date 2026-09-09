from typing import List


class Solution:
    def removeDuplicates(self,nums:List[int]) -> int:
        write_position = 1

        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[write_position] = nums[i]
                write_position +=1
                
            
        return write_position
    