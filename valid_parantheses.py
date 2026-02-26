class Solution:
    def isValid(self, s:str)-> bool:
        #Stack to store open brackets
        stack = []
        # Dictionary used to find corresponding open brackets for close brackets
        dictionary = {")": "(", "]": "[", "}":"{", }
        #Loop Through each characther in the string
        for char in s:
            # Check whether the character is an open bracket
            if char == "(" or char == "[" or char == "{":
                #if yes -> push to the stack
                stack.append(char)
            else:
                #if not open bracket, set the temporary variable as the matching opening bracket for the char
                matching_open = dictionary[char]
                # check if stack is empty, if yes, return False
                if len(stack)==0:
                    return False
                # If not empty, compare whether the matching opening bracket for the char is at the top of the stack
                if matching_open == stack[-1]:
                    #if yes, these 2 brackets are paired, so remove from stack
                    stack.pop()
                else:
                    return False
                
                
        return len(stack) ==0    
    
#Time complexity : O(n) -> Means the time grows proportionally with the input size
#Space complexity : O(n)


# When you run a Python file directly, Python sets a special variable called __name__ to "__main__".

# When you import that file from another file, __name__ is set to the module's name instead.

# So `if __name__ == "__main__":` means "only run this code if I'm running this file directly, not if someone is importing it."

# It's useful for putting test code that you don't want to run when the file is imported elsewhere.
if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("[[]]"))
    print(sol.isValid("[[]"))

    
    