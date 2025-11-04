from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
            
            if profit > max_profit:
                max_profit = profit
        return max_profit

#time complexity : O(n) -> just loop through the price list
#space complexity : O(1) -> no extra data structures
if __name__ =="__main__":
    solution =  Solution()
    print(solution.maxProfit(prices= [7,1,5,3,6,4]))