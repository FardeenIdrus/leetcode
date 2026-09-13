
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        
        smallest = float("inf")
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < smallest:
                smallest = prices[i]
            else:
                if prices[i] - smallest > max_profit:
                    max_profit = prices[i] - smallest

        return max_profit
    
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7,1,5,3,6,4]))
    print(sol.maxProfit([7,6,4,3,1]))
    print(sol.maxProfit([7,1,6,2,7]))
    
    
# Time complexity: O(n) - Each element in the input array is visited a maximum of once
# Space complexity: O(1) - No additional data structures are used, and max_profit and smallest, do not grow with the input size
# - they are constant