
class Solution:
    def maxScore(self, s:str) -> int:
       
       # Initialise pointer to check substrings
        left_pointer = 1 
        # Initialise left and right substring scores
        left_score = 0
        right_score = 0
        
        # Get the initial score of the first pair of substring by setting left substring as 1 character, and
        # right substring as len(s)-1 characters. Then count the number of 0's in the left substring, and number
        # of 1's in the right substring
        if s[0] == "0":
            left_score = 1
        
        for char in s[1:len(s)]:
            if char == "1":
                right_score +=1
                
        maximum_score = left_score + right_score
    
        #  Loop through the remaining splits (the first split was already scored above)
        #  "< len(s)-1" ensures that the right substring is never empty (minimum of 1 character)
        while left_pointer < len(s)-1:
            # s[left_pointer] is the first character of the right substring. This iteration moves it into the left substring
            # If it is a "0", the left substring gains a zero, so increment the left score
                if s[left_pointer] == "0":
                    left_score +=1
                # If it is a 1, the left substring has consumed a "1" from the right substring, thereby decreasing
                # the number of ones in the right substring. Therefore the right score is decremented
                else:
                    right_score -=1
                
                # Set the maximum score as the highest score acheived so far by the left and right substring scores
                maximum_score = max(maximum_score, left_score+right_score)
                # Increment pointer to check the next pair of non-empty substrings
                left_pointer +=1

        return maximum_score

# Time Complexity: O(n)
    # The for loop iterates through n-1 characters, where n is the number of characters in input string s. 
    # O(n-1) simplifies to O(n)
    # The while loop iterates from 1 to n-1 (n-2 characters), where n is the number of characters in input string s 
    # O(n-2) simplifies to O(n)
    # The two loops run one after the other, so their costs add: O(n) + O(n) = O(n)
    
# Space complexity: O(n), where n is the number of characters in input string s
    # s[1:len(s)] makes a copy of the string (strings are immutable objects), and the copy has n-1 characters
    # O(n-1) simplifies to O(n)
    # left_pointer, left_score, right_score, and maximum score are all constant size and do not grow with the input s
    # The 4 variables store integers, therefore the memory size they consume are constant

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxScore("011101"))
    print(sol.maxScore("00111"))
    print(sol.maxScore("1111"))