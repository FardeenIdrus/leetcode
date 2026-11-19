class Solution:
    def calPoints(self, operations: list[str]) -> int:
        
        # Initialise result variable to store the sum of scores
        result = 0
        # Initialise empty stack that will store the integer of string scores
        stack = []

        # Iterate through each string in the operations list
        for op in operations:
            
            # If the string is not an operation, then it is number, so push it into the stack
            if op != "+" and op != "D" and op!= "C":
                # Convert the string into an integer so the scores can be summed
                item = int(op)
                stack.append(item)

            # Constraints specify that : "For operation "+", there will always be at least two previous scores on the record", so we dont have to check that there is at least
            # 2 numbers in the stack
            # We need to obtain the previous 2 numbers from the stack, compute their sum, and push it into the stack
            # stack[-1] and stack[-2] obtains the last 2 numbers in the stack
            elif op == "+":
                x = int(stack[-1])
                y = int(stack[-2])
                total = x + y 
                stack.append(total)

            
            # "D" doubles the previous score and pushes the new score into the stack
            # So we obtain the score at the top of the stack without removing it ("D" adds a new score not modifies an existing one), double it's value, and assign it to a new variable
            # before pushing this new score into the stack
            elif op == "D":
                double = int(stack[-1]) *2
                stack.append(double)

            # "C" invalidates the previous score, so we remove the score from the stack by popping it
            elif op == "C":
                stack.pop()

        # Iterate through the stack while it is not empty, popping one element at a time, and adding the score to result
        while stack:
            result += stack.pop()

        # Return the total score
        return result

# N = number of strings in operations

# Time Complexity: O(N)
    # The for loop runs N times, once per string
    # Each run does O(1) work (a push, a pop, or reading the top of the stack)
    # Each operation pushes at most one item, so the stack never holds more than N items
    # The while loop pops each item once, so it runs at most N times, doing O(1) work each time
    # Total = O(N) + O(N) = O(N)

# Space Complexity: O(N)
    # The stack holds at most N items, since each operation pushes at most one item -> O(N)
    # result, item, x, y, total and double each hold one number -> O(1)
    # Total = O(N) + O(1) = O(N)