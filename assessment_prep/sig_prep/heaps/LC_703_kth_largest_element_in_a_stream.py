
import heapq
class KthLargest:
    
    # Runs once, when kthLargest (k, nums) is called
    def __init__(self, k: int, nums: list[int]):
        
        """ 
        Store k and the heap on the object so that add() can use them later
        # (plain variables like k and nums would be discared when __init__ ends)
        """
        self.k = k
        
        
        self.heap = nums
       
        """ Rearrange the list in place into a min-heap, so heap[0] is the smallest number """
        heapq.heapify(self.heap) 
        
        """ Keep only the k largest numbers: while there are more than k, remove the smallest
            The smallest of the k numbers left is the kth largest overall
        """
        heap_size = len(self.heap)
        while heap_size > self.k:
            heapq.heappop(self.heap)
            heap_size -=1
        
    # Runs each time add(val) is called: adds a new score and returns the kth largest
    def add(self, val: int) -> int: 
           # Fewer than k numbers so far: just add val
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        # Already k numbers: push val, then remove the smallest, in one step
        # The heap still holds the k largest numbers
        else:
            heapq.heappushpop(self.heap, val)

        # heap[0] is the smallest of the k largest, which is the kth largest
        return self.heap[0]
        

# Time complexity: __init__ is O(n log n), add is O(log k), where n is the length of nums and k is the k passed in
    # __init__: heapify(self.heap) -> O(n)
    # __init__: while loop pops at most n - k times, each heappop is O(log n) -> O(n log n)
    # __init__: the steps run one after the other, so their costs add: O(n) + O(n log n) = O(n log n)
    # add: len check and return self.heap[0] -> O(1)
    # add: heappush or heappushpop on a heap of at most k numbers -> O(log k)
    # add: O(1) + O(log k) = O(log k)

# Space complexity: O(k)
    # self.heap is the nums list itself, so no copy is made
    # After __init__ it holds at most k numbers, and add() never lets it grow past k -> O(k)
    # heap_size and val are single integers -> O(1)
    # Total: O(k)




