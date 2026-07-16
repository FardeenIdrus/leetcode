class Solution:
    def mergeAlternatively(self, word1:str, word2: str) -> str:
        
        result = []
        
        for i in range(min(len(word1), len(word2))):
            result.append(word1[i])
            result.append(word2[i])
            
        if len(word1) > len(word2):
            result.append((word1[len(word2):]))
        if len(word2) > len(word1):
            result.append(word2[len(word1):])
        
        return "".join(result)
    


if __name__ == "__main__":
    sol = Solution()
    print(sol.mergeAlternatively("abc", "pqr"))
    print(sol.mergeAlternatively("ab","pqrs"))
    print(sol.mergeAlternatively("abcd", "pq"))
    
#Time complexity: Accessing each item in both strings only once: O(n+m) where n and m are the lengths of the two strings

#Space complexity: O(n+m) where n and m are the length of the two strings