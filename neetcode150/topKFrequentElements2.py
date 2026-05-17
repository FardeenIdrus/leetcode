from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
    # Query = the top k frequent numbers (key), Value = The numbers that repeated k times
        dictionary = defaultdict(int)
        output_list = list()
        #+1 because index starts with 0. Edge case where all numbers are the same, e.g [1,1,1,1], we need index 4, not 3
        bucket_array = [[]for _ in range(len(nums)+1)]
    #first loop through the list of numbers and assign a count for each number. Key = number, Value = number of times it occured
        for i in range(len(nums)):
            dictionary[nums[i]] +=1
        
        #index = frequency, value = number 
        for i in dictionary:
            #at index i (frequency), append the number with that frequency
            bucket_array[dictionary[i]].append(i)
            #print(bucket_array)

        for i in range(len(bucket_array)-1,0,-1):
            if bucket_array[i]:
                for num in bucket_array[i]:
                    output_list.append(num)
                    if len(output_list) == k:
                        return output_list
                        

if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent([2,3,3,4,4,4,5,5,5], k = 3))

#Time complexity: O(n)
# Loop through each element in the input list once
#where n is the number of elements in the input array


#Space complexity: O(n) 
# where n is the number of elements in the input array
# dictionary holds up to m unique elements, and bucket_array has n+1 slots. In the worst case m = n, so O(n) overall. 
