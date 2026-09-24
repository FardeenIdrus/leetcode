from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # Count how many times each character appears in magazine
        dictionary_magazine = defaultdict(int)
        
       
        for i in magazine:
            dictionary_magazine[i] +=1

        # For each character needed in ransomNOte, check magazine has enough left
        for i in ransomNote:
            if dictionary_magazine[i] > 0:
                # Enough left - use one copy of this character
                dictionary_magazine[i] -=1
            else:
                # None let (or never existed - defaultdict returns 0 either way)
                return False
        # Every character in ransomNOte was successfully matched
        return True
    
    
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.canConstruct(ransomNote = "a", magazine = "b"))
    print(sol.canConstruct(ransomNote = "aa", magazine = "ab"))
    print(sol.canConstruct(ransomNote = "aa", magazine = "aab"))
    
# Time complexity: O(m + n), where m is the length of ransom note, and n the length of magazine
# We loop through each character in the input ransom note string, and input magazine string
# Each dictionary access is O(1) average, since dictionaries are hash-based

# Space complexity: O(n), where n is the number of unique characters in the input magazine string.
# In the worst case, all characters in magazine are unique
