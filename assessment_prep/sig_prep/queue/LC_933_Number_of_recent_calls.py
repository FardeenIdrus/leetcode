from collections import deque

class RecentCounter:

    # Runs once, when RecentCounter() is called
    def __init__(self):
        # Request times, oldest at the front, newest at the back
        self.queue = deque()

    # Runs each time ping(t) is called, where t is the time of the new request
    def ping(self, t: int) -> int:

        # Add the new request to the back
        self.queue.append(t)

        # Remove requests from the front that are older than t - 3000
        # while, not if: one new request can make several old requests expire at once
        while (self.queue[0] < t-3000):
            self.queue.popleft()

        # Every request left in the queue is inside the window [t - 3000, t]
        return len(self.queue)

# Time complexity: O(1) amortised per ping call, O(n) in total for n calls
    # self.queue.append(t): O(1)
    # One ping can remove many old requests, but each request is removed at most once, so removals can never exceed appends
    # Across n calls the removals total at most n -> O(n) in total
    # return len(self.queue): O(1)
    # The steps run one after the other, so one call costs O(1) + (its removals) + O(1), which is O(1) on average

# Space complexity: O(W)
# W = the number of pings in the queue at once, i.e. those within the last 3000 ms.
# Older pings are popped. t is strictly increasing, so W is at most 3001,
# which makes this effectively O(1).


if __name__ == "__main__":
    sol = RecentCounter()
    print(sol.ping(1))     # expect 1
    print(sol.ping(100))   # expect 2
    print(sol.ping(3001))  # expect 3
    print(sol.ping(3002))  # expect 3