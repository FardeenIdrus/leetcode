

class Solution:
    def mergeAlternatively(self, word1:str, word2:str) -> str:
        
        #string_list = list(str)
        merged_string = ''

        
        for i in range(min(len(word1), len(word2))):
            merged_string = merged_string + word1[i] + word2[i]
        
        merged_string = merged_string + word1[min(len(word1),len(word2)):] + word2[min(len(word1),len(word2)):]
            
        
        return merged_string


if __name__ == "__main__":
    sol = Solution()
    print(sol.mergeAlternatively("abc", "pqrs"))

#Time complexity: Accessing each item in both strings only once: O(n+m) where n and m are the lengths of the two strings

#Space complexity: No extra data struction used so O(1)