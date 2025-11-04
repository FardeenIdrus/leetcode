from typing import List
class Solution:
    def summaryRanges(self, nums: List[int])-> List[str]:
        start = nums[0]
        result = []
        end = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == end +1 :
                end = nums[i]
            else:
                if start == end :
                    result.append(str(start))
                else:
                    result.append(f"{start}->{end}")
                
                start = nums[i]
                end = nums[i]

        if start == end:
            result.append(str(start))
        else:
            result.append(f"{start}->{end}")
        return result
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.summaryRanges(nums = [0,1,2,4,5,7]))