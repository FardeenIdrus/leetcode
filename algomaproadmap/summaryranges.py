from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        ranges = list()
        
        
        if not len(nums):
            return ranges
        start_of_range = nums[0]
        for i in range(1,len(nums)):
            if nums[i-1] != nums[i]-1:
                if start_of_range == nums[i-1]:
                    ranges.append(str(start_of_range))
                else:
                    ranges.append(str(start_of_range) +"->" + str(nums[i-1]))
                start_of_range = nums[i]
            
        if start_of_range != nums[-1]:
            ranges.append(str(start_of_range) +"->" + str(nums[-1]))
        else:
            ranges.append(str(nums[-1]))

        return ranges

#Time complexity: O(n) -> where n is the length of the input List - O(1) operations inside the for loop and outside for loop
# Space compleixty: O(1) -> additional memory used is start_of_range which stores a single integer, therefore constant space

if __name__ == "__main__":
    sol = Solution()
    print(sol.summaryRanges([0,1,2,4,5,7]))
    print(sol.summaryRanges([0,2,3,4,6,8,9]))
    print(sol.summaryRanges([]))