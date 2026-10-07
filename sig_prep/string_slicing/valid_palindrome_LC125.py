
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left_pointer = 0
        right_pointer = len(s) -1

        while left_pointer <= right_pointer:
            # Check that both character from the left half and right half are alphanumeric
            if s[left_pointer].isalnum() and s[right_pointer].isalnum():
                # If they are both alphanumeric, check that both characters are the same. If they are the same, there is a match, so move one character inwards from both halfs
                if s[left_pointer].lower() == s[right_pointer].lower():
                    left_pointer +=1
                    right_pointer -=1
                # If the two characters are not equal - the string is not a valid palindrome
                else:
                    return False
            # The character from the left half is not alphanumeric - skip it and move to the next character
            elif not s[left_pointer].isalnum():
                left_pointer +=1
            # The character from the right half is not alphanumeric - skip it and move to the next character
            elif not s[right_pointer].isalnum():
                right_pointer -=1

        # All characters from the left half and right half matched - the string is a valid palindrome
        return True      
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))
    print(sol.isPalindrome("race a car"))
    print(sol.isPalindrome(" "))
    
# Time complexity: O(n), where n is the number of characters in s
    # Every iteration moves at least one pointer one step inward, so the pointers cross after at most n iterations
    # Each iteration does O(1) work: isalnum() and lower() on single characters, and one comparison

# Space complexity: O(1)
    # left_pointer and right_pointer are single integers
    # s[left_pointer].lower() creates a 1-character string, which is constant size
    # No copy of s is made