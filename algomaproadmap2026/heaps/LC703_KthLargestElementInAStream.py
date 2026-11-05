import heapq
class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        # Turn integer K into a persistent value that can be called by other methods in the class
        self.k = k
        # Initialise a heap storing all elements from nums
        self.heap = nums
        # Initialise a min-heap where the root element is guaranteed to be the smallest
        heapq.heapify(self.heap)

        # Ensure the min-heap has at most k elements
        # heapq.heappop(self.heap) runs n-k times when n > k
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:

        # If the heap has less than k elements, push the new element into the heap
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            # If the heap has k elements, push val in and remove the smallest element in one step
            # If val is smaller than heap[0], val is the one removed, so the heap is unchanged
            # If val is larger than heap[0], the old heap[0] is removed and val stays in the heap
            # heappushpop returns the element it removed, not the kth largest, so its result is not used here
            heapq.heappushpop(self.heap, val)

        # The heap holds the k largest elements, so the root (the smallest of them) is the kth largest
        return self.heap[0]

# Time complexity: O(n log n) for __init__ and O(log k) for each add call, where n is the number of elements in nums
    # __init__
        # heapq.heapify(self.heap) -> in-place transformation -> O(n)
        # while loop runs n-k times, each iteration does heapq.heappop(self.heap) -> O(log n) work
        # (n-k) * O(log n) = O((n-k) log n)
        # heapify and the while loop run one after the other, so costs add
        # O(n) + O((n-k) log n) = O(n + (n-k) log n) = O(n log n)
    # add
        # the heap never has more than k elements, so heappush or heappushpop -> O(log k)
        # return self.heap[0] -> O(1)
        # total per call = O(log k) + O(1) = O(log k)

# Space complexity: O(k), where k is the given k
    # self.k -> O(1). Integer that takes up constant space in memory
    # self.heap is built in place from nums, then trimmed to at most k elements -> O(k)
    # add never lets the heap grow beyond k elements
    # total = O(1) + O(k) = O(k)

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
