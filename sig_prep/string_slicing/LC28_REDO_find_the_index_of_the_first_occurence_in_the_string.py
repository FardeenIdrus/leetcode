

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        
        valid_range = len(haystack) - len(needle)
        
    
        for i in range(valid_range+1):
            counter = 0
            for j in range(len(needle)):
                if haystack[i+j] == needle[j]:
                    counter +=1
                
                if counter == len(needle):
                    return i
                    
        
        return -1
    
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.strStr("sadbutsad","sad"))
    print(sol.strStr("leetcode", "leeto"))
    
    