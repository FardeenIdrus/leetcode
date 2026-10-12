import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        
        # Convert nums into a heap with the smallest integer as the root node
        heapq.heapify(nums)

        # Get the size of the heap
        size = len(nums)
        # Iterate through the heap - removing (n-k) of the smallest elements
            # heappop removes the smallest element in the heap
            # When size == k, we have the k largest element
            # And the smallest of the k largest element is at the root node (nums[0])
        while size > k :
            heapq.heappop(nums)
            size -=1

        return nums[0]


# Time Complexity : O(n log n)
    # heapify(nums) -> O(n), where n is the number of integers in nums
    # heappop(nums) is called n - k times, each costing O(log n) -> O((n - k) log n)
    # Worst case is when k is small (e.g. k = 1): about n pops, so O(n log n)
    # Best case is when k = n: no pops, so only the O(n) heapify
    # The steps run one after the other: O(n) + O((n - k) log n) = O(n log n) in the worst case

# Space Complexity: O(1)
    # nums is directly transformed in place - no extra memory is used


if __name__ == "__main__":
    sol = Solution()
    print(sol.findKthLargest([3,2,1,5,6,4],2))
    print(sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4))