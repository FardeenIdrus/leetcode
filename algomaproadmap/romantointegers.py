

class Solution:
    def romanToInt(self, s: str) -> int:
        
        mapping_dict = {"I": 1, "V":5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        integer = 0 
        
        for i in range(len(s)-1):
            if mapping_dict[s[i]] < mapping_dict[s[i+1]]:
                integer = integer - mapping_dict[s[i]]
            else:
                integer = integer + mapping_dict[s[i]]
        integer = integer + mapping_dict[s[-1]]

        return integer
        
        
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToInt("VI"))
    print(sol.romanToInt("MCMXCIV"))
    
# Time complexity = O(n)
# O(n) : Each item in the input string is accessed only once. n is the length of input string

#Space complexity: O(1) 
# constant size dictionary