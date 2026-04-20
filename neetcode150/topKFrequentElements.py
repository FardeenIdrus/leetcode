from typing import List 
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums:List[int], k:int) -> List[int]:
        #initialise dict
        dictionary = defaultdict(int)
        #list returning the top k frequent elements
        output_list = list()
        for i in range(len(nums)):
            #increment count for num[i]. key = number, value = count of the number
            dictionary[nums[i]] +=1    
            #create a new dictionary as a tuple in descending order of frequency
            #dictionary.items() = returns the (key,value) pair as tuples
            # key = lambdax:x[1] sorts by the second element in the tuple (the count)
            #reverse = True : sorts by descending order of the count    
        new_dict = sorted(dictionary.items(), key = lambda x:x[1], reverse = True)
        for i in range(k):
            #append the top k numebers
            #[i][0]. i -> points to which tuple, [0] -> points to index 0 in tuple i
            output_list.append(new_dict[i][0])
        return output_list
           

#Time complexity: O(n log n)
     
        # O(n) -> for looping through each element in the array
        # O(n log n) -> for sorting 
        # O(n) dominates

#Space complexity: dictionary can hold up to n distincty numbers -> O(n) 
                    # output list holds k numbers and since k<= n, the dominant term is O(n)
#Space complexity = O(n)


if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent([1,2,2,3,3,3,4], 2))