from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs:list[str]) -> list[list[str]]:
        
        # Initialise a dictionary where the key is the sorted string, and values are the input strings that are anagrams
        # of each other grouped together in a list
        anagram_dict = defaultdict(list)
        
        # Loop through each string in strs
        for i in range(len(strs)):
        # Strings that are anagrams of each other will have the same sorted string
            sorted_string = "".join(sorted(strs[i]))
        # Append the original string as a value to the key of the sorted string
        # Strings that are anagrams of each other will have the same sorted string, so they will be added
        # as a value to the same key in the dictionary
            anagram_dict[sorted_string].append(strs[i])
        
        
       
        return list(anagram_dict.values())
            

if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(sol.groupAnagrams([""]))
    
# Time complexity: O(n . k log k) where n is the number of strings in strs, and k the number of characters in the longest string
# The program iterates through each strings in strs once -> O(n)
# sorted() is a out of place transformation and takes O(k log k), where k is the length of the longest string in strs

# Space complexity: O(n·k), where n is the number of strings in strs, and k the number of characters in the longest string. 
# In the worst case (no two strings are anagrams), the dictionary holds up to n distinct keys (each a sorted string) and n total values (the originals) spread 
# across all groups. 
# Each string takes space proportional to its length, so total space scales with n strings × k characters each.