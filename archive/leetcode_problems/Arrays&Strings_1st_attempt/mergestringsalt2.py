

class Solution:
    def mergeAlternatively(self, word1:str, word2:str) -> str:
        merged_string=  ''
        
        for i in range(min(len(word1), len(word2))):
            merged_string = merged_string + word1[i] +word2[i]
        
        merged_string = merged_string + word1[min(len(word1),len(word2))::] + word2[min(len(word1),len(word2))::]
        
         
        return merged_string
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.mergeAlternatively('abc','pqrst'))

# Time complexity: O(n+m) - Accessing each item in both strings once
# n+m is the length of the input strings

# Space complexity: O(1) - no extra data structure used 