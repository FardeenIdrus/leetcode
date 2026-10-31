
class Solution:
    def strStr(self, haystack:str, needle:str) -> int:
        
        # Last index in haystack where needle could still start
        # A later start leaves fewer than len(needle) characters, so a match is impossible
        valid_range = len(haystack) - len(needle)
        
        # i is the index in haystack where each attempt to match needle starts
        # E.g. haystack = "haystack", needle = "stack": starting at "t" (index 4) leaves
        # only 4 characters, fewer than the 5 needed
        
        for i in range(0, valid_range + 1):
            # Each attempt starts matching from needle[0], so reset the count of matched characters
            pointer = 0
            
            # j is the position in needle, so haystack[i + j] is the haystack character lined up with needle[j]
            for j in range(len(needle)):
                if haystack[i + j] == needle[j]:
                    pointer += 1
                    # All characters of needle matched, so needle starts at index i
                    if pointer == len(needle):
                        return i
                else:
                    # Mismatch: abandon this start index and try the next one
                    break
        
        # No start index matched all of needle
        return -1
    

# Time complexity: O(M x N), where M is the length of haystack and N is the length of needle
    # The outer for loop tries each possible start index: M - N + 1 attempts, which is at most M
    # The inner for loop compares up to N characters per attempt, doing O(1) work each
    # Worst case: most attempts match nearly all of needle before failing, so the costs multiply: at most M x N comparisons

# Space complexity: O(1)
    # valid_range, pointer, i and j are single integers, constant in size
    # No extra data structures are used
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.strStr("sadbutsad", "sad"))
    print(sol.strStr("leetcode", "leeto"))
    print(sol.strStr("testing", "ing"))