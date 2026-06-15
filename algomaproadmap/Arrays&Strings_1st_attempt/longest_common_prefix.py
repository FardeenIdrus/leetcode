from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = ""
        # Get the shortest word in the list of words
        shortest = len(min(strs, key = len))
        # Loop through each chracter in the first word until length of shortest word to avoid index out of range error
        for i in range(shortest):  
            # For each character, compare with the other words in the list, (1,len(strs)) since we dont need to compare
            # with the first word itself
            for j in range(1,len(strs)):
    
                if strs[0][i] != strs[j][i]:
                    return prefix
            
            prefix += strs[0][i]
        return prefix

# Time complexity: O(m*n)
    # Total iteration of outer loop * total iteration of inner loop
    # O(1) expressions inside nested loop
    # = m *n where m is the shortest word in input list, and n is the number of words in the input list
    # = O(m*n)

#Space complexity: O(m) where m is the length of the shortest word in the input list
# Worst case is all strings in the input list are the same length 
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix(["flower","flow","flight"]))
    print(sol.longestCommonPrefix(["dog","racecar","car"]))
    print(sol.longestCommonPrefix(["ab","a"]))
    print(sol.longestCommonPrefix(["flower","flower","flower","flower"]))
