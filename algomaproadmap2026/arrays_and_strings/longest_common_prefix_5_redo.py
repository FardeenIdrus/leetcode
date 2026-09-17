from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # The longest common prefix possible is the length of the shortest word in the input array
        shortest_word = (min(strs, key = len))
        # Pointer to track the longest prefix
        pointer = 0 
        
        # Loop through each character from index 0 to index shortest word - where shortest word is the index of the 
        # last character of the shortest word in the input array
        for column in range(len(shortest_word)):
            # Loop through each word
            for word in range(1,len(strs)):
                # Compare each character in each word in the input array at index column to each other
                # Any word in the input array can be used as the reference, as a common prefix will be 
                # Shared by all words.
                # Check if the characters match in the column
                if strs[word][column] != strs[0][column]:
                # If they do not match, return the characters up to the point before the mismatch
                    return shortest_word[:pointer]
            # the return statement above would only fire if there was a mistmatch. If there was no mismatch,
            # we check the next character at the next column in all words 
            pointer +=1   
        
        # Would only fire when there is no mismatch, meaning the longest common prefix is the shortest word.
        # All characters up to and including the final character of the shortest word match across all. 
        # words in the array. 
        return shortest_word


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix(["flower","flow","flight"]))
    print(sol.longestCommonPrefix(["dog","racecar","car"]))
    
# Time complexity: O(s x w) - where s is the length of the shortest word in the input array, and w
# is the number of words in the input array. In the worst case - all words are identical in length, and therefore,
# all characters in the array will be checked

# Space complexity: O(1) - No extra data structure is used. shortest_word references an existing string
# from strs rather than allocating new memory, and pointer is a single constant-size integer