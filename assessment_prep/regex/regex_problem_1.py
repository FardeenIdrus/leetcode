import re
from collections import Counter


class Solution:
    def return_email(self, text: str) -> list[str]:
        matches = re.findall(r"[\w.-]+@[\w.-]+\w+", text)
        
        
        return matches
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.return_email("Contact john@example.com or jane.doe@company.co.uk. for details"))

k = re.findall(r"[.*]" ,"test test")
print(k)