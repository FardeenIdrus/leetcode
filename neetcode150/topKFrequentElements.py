from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
    # Query = the top k frequent numbers (key), Value = The numbers that repeated k times
        dictionary = defaultdict(int)
        output_list = []
    #first loop through the list of numbers and assign a count for each number. Key = number, Value = number of times it occured
        for i in range(len(nums)):
            dictionary[nums[i]] +=1
        
    
        sorted_dict = sorted(dictionary.items(), key = lambda x:x[1], reverse = True)
        
        for i in range(k):
            output_list.append(sorted_dict[i][0])
        return  output_list
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent([1,2,2,3,3], k = 2))

#Time complexity: O(n log n) -> worst case where all elements are unique

#first for loop : Access each element in the dictionary once and increment count -> O(n)
#sort function : sorting items by their count : O(m log m) where m is the number of unique elements
# O(m log m) dominates

#Space complexity: O(m) 

# dictionary of size m (number of unique elements)
# worst case m = n (all elements are unique)