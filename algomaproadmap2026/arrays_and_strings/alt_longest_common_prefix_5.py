
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        shortest_word = min(strs, key = len)
    
        # Loop through each column from 0, to the last column of the shortest word
        for column in range(len(shortest_word)):
        # Loop through each word in the input array
            for j in range(len(strs)):
        # If character at position column does not match the character at position column in word j
        # return the characters that matched up till position column
                if strs[0][column] != strs[j][column]:
                    return shortest_word[0:column]
                    
        # Return statement only fires when there is no mismatch in the inner loop, therefore the return statement
        # in the inner loop never fires - so there were no mismatch and the shortest word is the longest prefix
        return shortest_word
    


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix(["flower", "flow", "flight"]))
    print(sol.longestCommonPrefix(["dog", "racecar", "car"]))
    print(sol.longestCommonPrefix(["abab", "aba", ""]))
    

# Time complexity : O(n x s): where n is the number of words in the input array, and s is the length of the shortest word
# in the input array - In the worst case, all words are of equal length, so each character in each word would need to be checked

# Space complexity: O(1) -  No extra data structure is used. If counting the output - then O(s) because in the worst case
# all words are identical, and the entire word is returned, where m is the length of the shortest word