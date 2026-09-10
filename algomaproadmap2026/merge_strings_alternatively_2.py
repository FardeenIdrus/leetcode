

class Solution:
    def mergeAlternately(self, word1, word2: str) -> str:
        
        merged_string = []
        
        for i in range(min(len(word1),len(word2))):
            merged_string.append(word1[i] + word2[i])
        
        
        if len(word1)> len(word2):
            longest_word = word1
            merged_string.append(longest_word[len(word2)::])  
        elif len(word2) > len(word1):
            longest_word = word2 
            merged_string.append(longest_word[len(word1)::])

         
    
        return "".join(merged_string)



if __name__ == "__main__":
    sol = Solution()
    print(sol.mergeAlternately("abc", "pqr"))
    print(sol.mergeAlternately("ab", "pqrs"))
    print(sol.mergeAlternately("abcd", "pq"))
    
# Time complexity: Assessing each item in both strings once  -> O(n+m) where n and m are the lengths of the two input strings
# Space complexity: O(n+m) where n aand m are the length of the two strings. The length of merged_string grows with the input strings