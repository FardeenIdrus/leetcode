import heapq
from collections import Counter 
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        min_heap = []

        # Dict {number: frequency}
        c = Counter(nums)
        
        for number, frequency in c.items():
            # If the heap is smaller than k, we push
            # numbers in regardless of frequency
            if len(min_heap) < k:
                heapq.heappush(min_heap, (frequency, number))

            else:
            # Once the heap is of size k, we want to only add new
            # numbers with a larger frequency than a number
            # currently in the heap
            # If the new number has a lower frequency - it is
            # immediately popped and removed
            # If the number has a higher frequency than the lowest
            # in the heap, the number with the larger frequency
            # is pushed, and the number with the smallest frequency
            # is popped and removed from the heap
                heapq.heappushpop(min_heap, (frequency, number))

        # Format the output to return a list of the k most frequent numbers
        res = []
        # Iterate through each tuple in min_heap (min_heap now contains the k most frequent elements)
        for num in min_heap:
            # and append the "number" element to the result array
            res.append(num[1])

        return res
    
    
# Time complexity: O(n + m log k), where n is the number of integers in nums, m is the number of distinct integers and k is the k given
    # c = Counter(nums) -> O(n), goes through each integer in nums once
    # for number, frequency in c.items() -> m iterations, one per distinct integer
    # heappush (first k iterations) and heappushpop (remaining m - k iterations) -> O(log k) each, because the heap never holds more than k items
    # All m iterations -> O(m log k)
    # Building res -> loops over k tuples -> O(k)
    # The steps run one after the other, so their costs add: O(n) + O(m log k) + O(k) = O(n + m log k)
    # Worst case is when every integer is distinct (m = n): O(n log k)

# Space complexity: O(m)
    # c -> m entries -> O(m)
    # min_heap -> at most k tuples -> O(k)
    # res -> k numbers -> O(k)
    # k is at most m, so O(m) + O(k) + O(k) = O(m), which is O(n) in the worst case


if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent([1,1,1,2,2,3],2))
    print(sol.topKFrequent([1],1))
    print(sol.topKFrequent([1,2,1,2,1,2,3,1,3,2],2))
    