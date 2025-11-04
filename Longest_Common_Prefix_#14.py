from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Find the shortest string
        min_length = min(len(s) for s in strs)
        result = ""
        
        # Loop through each character of the shortest string
        for char in range(min_length):
            # Loop through each string in the list
            for i in range(len(strs)):
                # Check if all strings have the same character at this position
                if strs[i][char] != strs[0][char]:
                    return result
            
            # All strings matched at this position, add character to result
            result += strs[0][char]
        
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonPrefix(strs=["flower", "flow", "flight"]))
    print(solution.longestCommonPrefix(strs=["dog", "racecar", "car"]))

                    
            
                