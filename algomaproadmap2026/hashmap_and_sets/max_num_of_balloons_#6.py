from collections import defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        # Counts how many times each relevant letter appears in text
        text_dict = defaultdict(int)
        
        # How many of each letter ONE "balloon" needs (l and o need 2, the rest need 1)
        balloon_characters = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}

        # Only count letters that actually appear in "balloon" - ignore everything else
        for i in text:
            if i in balloon_characters:
                text_dict[i] += 1

        # For each letter needed to spell "balloon":
        for i in balloon_characters:
            # Not enough of this letter to spell "balloon" even once - answer is 0
            if text_dict[i] < balloon_characters[i]:
                return 0
            else:
                # How many balloons this letter alone could support -
                # e.g. 6 l's available, 2 needed per balloon -> enough for 3 balloons from l's
                text_dict[i] = text_dict[i] // balloon_characters[i]
                                

        return min(text_dict.values())
    
if __name__ == "__main__": 
    
    sol = Solution()
    print(sol.maxNumberOfBalloons("nlaebolko"))
    print(sol.maxNumberOfBalloons("loonbalxballpoon"))
    print(sol.maxNumberOfBalloons("leetcode"))

# Time complexity : O(n+m), where n is the number of characters in text, and m the number of unique characters
# in the word "balloon"
    #  We loop through each character in the input text string, and loop through each unique character in balloon
    
# Space complexity: O(m) - where m is the number of unique characters in the word balloon
    # We store 2 dictionaries - one to store the required count of each character to store the word balloon
    # One to store the count of each character in the text string that can be used to form the word balloon
    # We only insert a new key into the dictionary if the character is in the word balloon, so in the worse case
    # where the text string has all the characters needed to form the word balloon, the dictionary will store
    # at most the number of unique characters in balloon