from collections import deque 

class RecentCounter:
    
    def __init__(self):
        self.counter = 0
        
        self.queue = deque()
                
    def ping(self, t: int) -> int:
        # Add the new call to the queue
        self.queue.append(t)
        
        # Check for any calls in the queue that are older than t-3000
        while self.queue[0] < t-3000:
            # If any elements in the queue are older than t-3000, remove them from the queue
                self.queue.popleft()
        
        # Only calls that are greater than or equal to t-3000 will be left in the queue
        # hence we can simply return the length of the queue
        return len(self.queue)

if __name__ == "__main__":
    sol = RecentCounter()
    sol.ping(1)
    sol.ping(100)
    sol.ping(3001)
    sol.ping(3002) 
    
    