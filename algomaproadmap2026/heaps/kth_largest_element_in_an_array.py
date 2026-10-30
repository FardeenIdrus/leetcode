import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        
        heapq.heapify(nums)
        
        while len(nums) > k:
            heapq.heappop(nums)
        
    
        return nums[0]

if __name__ == "__main__":
    sol = Solution()
    print(sol.findKthLargest([3,2,1,5,6,4],2))
    print(sol.findKthLargest([3,2,3,1,2,4,5,5,6],4))
    
# Time Complexity: O(n log n)
    # heapq.heapify(nums) -> O(n), where n is the number of integers in nums
    # heapq.heappop is called at most n-k times (since the heap will keep at least k elements), and each operation costs
    # O(log n), so O((n-k) log n)
    # Worst case is when k is small (e.g, k= 1): about n pops so O(n log n)
    # Best case is when k=n, no pops only O(n) heapify
    # The steps run one after the other : O(n) + O((n-k) log n) = O(n log n) in the worst case
    


# Space Complexity: O(1)
    # heapq.heapify(nums) is an in-place transformation, so no extra memory is used
    # nums[0] is the output integer, which is constant in size -> O(1)
    # Typically we exclude the return value from
    # time and space complexity 