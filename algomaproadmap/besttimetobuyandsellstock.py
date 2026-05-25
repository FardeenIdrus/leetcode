from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        smallest = prices[0]
        profit = 0
        for i in range(len(prices)):
            if prices[i] < smallest:
                smallest = prices[i]
            else:
                if (prices[i] - smallest) > profit:
                    profit = prices[i] - smallest

                        
        return profit

#Time complexity: O(n) where n is the number of elements in the prices array
#Space complexity: O(1) - additional memory use are smallest and profit which are integers - hence constant space
# since the variable does not grow with input size. 

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7,1,5,3,6,4]))
    print(sol.maxProfit([7,6,4,3,1]))
    print(sol.maxProfit([2, 4, 1]))
    
