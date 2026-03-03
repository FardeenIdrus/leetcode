from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Creates a dictionary where any new key automatically gets an
        # empty list [] as its default value. This avoids KeyError
        # when appending to a key that doesn't exist yet
        anagram_map = defaultdict(list)
        #An empty list that will hold the final grouped anagrams.
        result = []
        
        for s in strs:
            # anagrams produce the same sorted tuple, so they'll map to the same key
             sorted_string = tuple(sorted(s))
             #Appends the original string to the list at that key. So "eat", "tea", and "ate" all land under key ('a', 'e', 't').
             anagram_map[sorted_string].append(s)
             
        for value in anagram_map.values():
            result.append(value)
        return result
        
if __name__ == "__main__":
    sol = Solution()
    