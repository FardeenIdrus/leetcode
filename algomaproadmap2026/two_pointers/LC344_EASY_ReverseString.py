class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Initialise left and right pointes
        left_pointer = 0
        right_pointer = len(s)-1

        # Execute the code inside the loop while the right_pointer is greater than or equal
        # the left pointer 
        while left_pointer <= right_pointer:
            # Store the character at the left and right pointers so that when swapping
            # the characters from one end to the other - we do not lose one of the swapped
            # characters
            left_char = s[left_pointer]
            right_char = s[right_pointer]
            
            # Set the character at the left pointer to the character at the right pointer
            # (swap from one end to the other)
            s[left_pointer] = right_char
            s[right_pointer] = left_char
            
            # Update the pointers to move inwards from both directions 
            left_pointer +=1
            right_pointer -=1

        return s

# Time Complexity: O(n), where where n is the number of characters in s
    # The while loop executes exactly n/2 times -> O(n/2)
    # Each operation inside the while loop (assignment, and arithmetic) are O(1) operations -> O(1)
    # Total = O(n/2) * O(1) = O(n/2) 
    # O(n/2) simplifies to O(n)

# Space Complexity: O(1)
    # left_pointer, right_pointer, left_char, right_char take constant memory -> O(1)

if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseString(["h","e","l","l","o"]))
    print(sol.reverseString(["H","a","n","n","a","h"]))