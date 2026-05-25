
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        pointer1 = 0
        if not s:
            return True
        else:
            for i in range(len(t)):
                if t[i] == s[pointer1]:
                    pointer1 +=1 
                    if pointer1 == len(s):
                        return True
            
        
        
        
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.isSubsequence("abc","ahbgdc"))
    print(sol.isSubsequence("axc", "ahbgdc"))
    
# Time complexity: O(n) where n is the length of string t

# Space complexity: O(1) - additional memory used is pointer 1 which is an integer - hence constant space