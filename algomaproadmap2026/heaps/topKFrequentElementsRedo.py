import heapq 
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums:list[int], k: int) -> list[int]:
        
        # Initialise a default dict with Key: number, Value: Count of how many times the number is in nums
        count_dict= defaultdict(int)
        
        min_heap = []
        res= []
        
        for num in nums:
            count_dict[num]+=1
            
        for num, freq in count_dict.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (freq, num))
                
            else:
                heapq.heappushpop(min_heap, (freq, num))
                
        
        for number in min_heap:
            res.append(number[1])
            
        return res
    

if __name__== "__main__":
    sol = Solution()
    print(sol.topKFrequent([1,1,1,2,2,3], 2))
    print(sol.topKFrequent([1], 1))
    print(sol.topKFrequent([1,2,1,2,1,2,3,1,3,2],2))

# Time complexity: O(n + m log k)
# n = number of elements in nums, m = number of distinct elements in nums, k = number of elements to return
    # Build the dictionary: loop over n elements, O(1) each -> O(n)
    # Loop over the m dictionary items, one heap push or pushpop each, O(log k) per operation -> O(m log k)
    # Build res from the heap: at most k elements, O(1) each -> O(k)
    # Total: O(n) + O(m log k) + O(k) = O(n + m log k), since k <= m

# Space complexity: O(m)
# m = number of distinct elements in nums, k = number of elements to return (k <= m)
    # Dictionary: O(m)
    # min_heap: at most k elements -> O(k)
    # res: at most k elements -> O(k)
    # Total: O(m) + O(k) + O(k) = O(m), since k <= m
    