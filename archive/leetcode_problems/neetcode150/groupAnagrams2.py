from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #defaultdict assigns a 
        #default value to keys that do not exist
        # which means no need to manually check for missing keys with a default empty list
        dictionary = defaultdict(list) 
        
        for i in range(len(strs)):
            sorted_word = tuple(sorted(strs[i])) 
            dictionary[sorted_word].append(strs[i])
            
        return list(dictionary.values())
                
if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(['cat', 'tac', 'stop', 'tops']))
    
#k = length of longest string
# n = number of strings
#Time complexity: O(n *k log k) : For n strings,for each one, you sort it which costs O(k log k) and we are doing the
#sort operation n times. 

#Space complexity: O(n*k): dictionary stores all the original strings. You have n strings each of length k