from typing import List
from collections import defaultdict
class Solution:
     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         anagram_dict = defaultdict(list) 
         for i in range(len(strs)):
             anagram_dict[tuple(sorted((strs[i])))].append(strs[i])
        
         return list(anagram_dict.values())
     
if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["bad","dab","adb","cat"]))
    


