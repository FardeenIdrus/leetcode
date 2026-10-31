
from collections import defaultdict
class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        
        
        good_pair = defaultdict(int)
        number_of_pairs = 0 
        for i in range(len(nums)):
            # Index of the integer subtracted by the integer
            number_of_pairs += len(nums) - (i+1)
            
            index_value_gap = i - nums[i]
            
            good_pair[index_value_gap] +=1 

        for key in good_pair:
            number_of_pairs -= (good_pair[key] * (good_pair[key]-1) // 2)

        return number_of_pairs
    
# Time complexity: O(n) where n is the number of integers in nums
# of unique (index - value) pairs
    # The first for loop iterates through each integer in nums -> O(n), and does O(1) work
    # The second for loop iterates through each key in the dictionary (in the worst case each index value gap
    # is distinct -> O(n)), and does O(1) work
    # O(n) + O(n) = O(n)

# Space complexity : O(n)
    # The dictionary good_pair in the worst case contains up to n values (in the worst case, each index value
    # gap in nums is distinct - so the dictionary stores n values) -> O(n)
    # number_of_pairs and i are constants and do not grow with the input nums -> O(1)
    # O(n) + O(1) = O(n)

    

if __name__ == "__main__":
    sol = Solution()
    print(sol.countBadPairs([4,1,3,3]))
    print(sol.countBadPairs([1,2,3,4,5]))