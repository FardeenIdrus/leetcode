from typing import List
class Solution:
    def topKFrequent(self, nums:List[int],k: int )-> List[int]:
        frequency_map = {}
        for i in range(len(nums)):
            if nums[i] in frequency_map:
                frequency_map[nums[i]] +=1
            else:
                frequency_map[nums[i]] = 1

        bucket =  [[] for _ in range(len(nums)+1)]
        for i in frequency_map:
            bucket[frequency_map[i]].append(i)
        
        result = []
        for i in range(len(bucket)-1, 0, -1):
            if bucket[i]:
                result.extend(bucket[i])
                if len(result)>=k:
                    return result
            
            
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent([1,2,2,3,3,3],2))        