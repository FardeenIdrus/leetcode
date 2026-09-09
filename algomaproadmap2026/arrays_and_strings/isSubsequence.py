
class Solution:
    def isSubsequence(self, s: str, t:str) -> bool:
        pointer_s = 0
        pointer_t = 0
        
        # If s is empty, it is a subsequence of any string -> so return True
        if not s:
            return True
        
        
        # Loop through each character in t
        for i in range(len(t)): 
                # If there is a match, move pointer to the next character of s and t
                if t[i] == s[pointer_s]:
                    pointer_s+=1
                    pointer_t +=1
                    # If pointer s = len(s), that means all characters in s have been matched with characters in t
                    if pointer_s == len(s):
                            return True
                else:
                        # If there is no match, check the next character in t
                    pointer_t +=1
                
        return False
    

# Time complexity: O(n)- where n is the number of characters in input string t. Worst case is when the last character of 
# s matches the last character of t

# Space complexity: O(1) -> Additional memory used are pointer_s and pointer_t which are constant in size and do not grow
# with input s and i

if __name__ == "__main__":
    sol = Solution()
    print(sol.isSubsequence("abc", "ahbgdc"))
    print(sol.isSubsequence("axc", "ahbgdc"))    
    
