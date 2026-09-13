class Solution:
    def isSubsequence(self, s:str, t: str) -> bool:
        
        # Initialise a pointer to track the position of characters in string s
        pointer_s = 0
        #Empty string is a subsequence of any string, so return true 
        if not s:
            return True
        
        # Loop through each character in string t
        for i in range(len(t)):
            #Check whether the character at position i in string t is equal to the character at position s in string s
            if t[i] == s[pointer_s]:
            # If they are a match, move to the next character in both strings to compare whether the next characters in 
            # both input strings are equal
                pointer_s +=1
        
                   
        # If pointer s is equal to the length of string s, that means that s is exactly a subsequence of t, since all
         # characters in string s is in string t 
            if pointer_s == len(s):
                return True
        # Otherwise return False, as not all characters in string s is in string t
        return False
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.isSubsequence("b", "abc"))
    print(sol.isSubsequence("abc", "ahbgdc"))
    print(sol.isSubsequence("axc", "ahbgdc"))
    
# Time complexity: O(n), where n is the the number of characters in string t. We visit each character in string t a maximum 
# of one time

# Space complexity : O(1) - No extra data structure is used, and pointer_s is a constant that do not grow with the input size