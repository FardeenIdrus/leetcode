class Solution:
    def isSubsequence(self, s:str, t:str) -> bool:
       S = len(s)
       T = len(t)
       
       if s == '': return True
       if S > T: return False
       
       j = 0
       for i in range(T):
            if t[i] == s[j]:
                if j == S-1:
                    return True
                j +=1
       return False
    
        
#Time: O(T) -> cause we are going through the string t
#Space: O(1) -> cause we are not using any data structures

if __name__ == "__main__":
    solution = Solution()
    print(solution.isSubsequence(s="abc",t="ahbgdc"))

'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
'''