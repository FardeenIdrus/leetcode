from collections import defaultdict

class Solution:
    def romanToInt(self, s:str) -> int: 
        num_dict = {"I":1, "V":5, "X":10, "L": 50, "C": 100, "D": 500, "M":1000}
        
        total = 0
        
        for i in range(len(s)-1):
            if num_dict[s[i]] < num_dict[s[i+1]]:
                total -= num_dict[s[i]]
            else:
                total += num_dict[s[i]] 
        
        total += num_dict[s[-1]]
    
        return total
if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToInt("IV"))
    print(sol.romanToInt("III"))
    print(sol.romanToInt("LVIII"))
    print(sol.romanToInt("MCMXCIV"))
        
        
# Time complexity: O(n) -> Single pass through the string, constant work per character. Dictionary look up is O(1)

# Space complexity : O(1) -> Mapping dictionary does not grow with input size 
# num_dict has a fixed 7 entires regardless. of input size
#test