from collections import defaultdict
class Solution:
    def subarraySum (self, nums: list[int], k: int) -> int:
        
        prefix_sum_counter  = defaultdict(int)

        prefix_sum_counter[0] =1 
        prefix_sum= 0

        counter = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]

            if (prefix_sum - k) in prefix_sum_counter:
                counter+= prefix_sum_counter[prefix_sum -k]

            prefix_sum_counter[prefix_sum] +=1

        return counter        
        
    
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.subarraySum([1,1,1], 2))
    print(sol.subarraySum([1,2,3], 3))

