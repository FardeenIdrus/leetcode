class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        parantheses_dict = {")": "(", "}": "{", "]": "["}
        
        for p in s:
            if p == "(" or p == "[" or p == "{":
                stack.append(p)

            elif p == ")" or p == "]" or p == "}":
                if not stack or stack[-1] != parantheses_dict[p]:
                    return False
                else:
                    stack.pop()

                
        if not stack:
            return True
        
        else:
            return False
        

# Time Complexity: O(N), where N is the number of characters in s
    # For loop run N times, where N is the number of characters in s -> O(N)
        # Each run of the for loop does O(1) work (dictionary lookups, append, pop) -> O(1)
    # "if not stack": is an O(1) check that runs once at the end of the program -> O(1)
    # Total = (O(N) * O(1)) + O(1) = O(N)

# Space Complexity: O(N) where N is the number of characters in s
    # In the worst case, stack stores at most N characters. This occurs when every character in s is an open bracket -> O(N)
    # parantheses_dict stores a constant number of (key, value) pairs and is never updated (only used for look ups) -> O(1)
    # Total -> O(N) + O(1) = O(N)
