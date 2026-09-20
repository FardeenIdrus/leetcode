import re

from collections import Counter
from typing import List

# No class solution

def extract_numbers(text:str) -> List[str]:
    
    matches = re.findall(r"\d{3}-\d{3}-\d{4}", text)
    return matches

test_string = f"test case 1:" "Call me at 555-123-4567 or the office at 800-555-0199 anytime"

print(extract_numbers(test_string))


# Solution with List of Numbers as Input, and you have to iterate through
class Solution:
    def extract_phone_numbers(self, text: List[str]) -> List[str]:
        
        numbers = []
        for number in text:
            numbers.extend((re.findall(r"\d{3}-\d{3}-\d{4}", number)))
        
        return numbers
    



if __name__ == "__main__":
    sol = Solution()
    print(sol.extract_phone_numbers(["Call me at 555-123-4567 or the office at 800-555-0199 anytime",
                                    "Call me at 555-123-4567 or the office at 800-555-0199 anytime"]))
    


lst = [1,2,3,4]
squared = [val**2 for val in lst]
print(squared)
    