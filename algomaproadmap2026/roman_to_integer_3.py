
class Solution:
    def romanToInt(self, s:str) -> int:
        
        dictionary = {"I":1, "V":5, "X": 10, "L": 50, "C":100, "D":500, "M": 1000}  
        # Initialise total
        total = 0
        
        # Loop through each character in the input string except for the last character, so that the i+1 operation does not raise
        # index out of range error
        for i in range(len(s)-1):
            
            # Roman numerals go from largest to smallest, so if a smaller number comes before a larger one, it is a subtract operation
            if dictionary[s[i]] < dictionary[s[i+1]]:
                # e.g) IV = 5-1 = 4. Subtract the smaller number from the bigger number. However if the input string is just IV, total
                # would initially be -1 here.
                total -= dictionary[s[i]]
            
            else:
            # If larger number comes before smaller number as normal, simply add that number to the total
                total += dictionary[s[i]]
        # Since the loop only iterates to (len(s)-1), we add the final character outside the loop    
        # In the "IV" example, total = -1 + 5 = 4, as expected
        total += dictionary[s[-1]]
        
        return total

# Time complexity: O(n), where n is the number of characters in the input string. We loop through each character only once
# Space complexity : O(1). No extra data structure is used, and the variable total does not grow with input size
# Dictionary look up time is O(1) per character, when accessing elements by Key

if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToInt("III"))
    print(sol.romanToInt("LVIII"))
    print(sol.romanToInt("MCMXCIV"))
    
    