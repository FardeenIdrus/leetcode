class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        # Idea: walk through s one character at a time, dropping each character into the row it lands on
        # in the zigzag. The row number goes down to the last row, then back up to row 0, and repeats.
        # At the end, read the rows from top to bottom.
        
        # string_list[row] holds the characters that land on row r, in the order they are visited
        string_list = [[] for _ in range(numRows)]
        
        # The row the current character goes into (starts at the top row, 0)
        row_counter = 0
        
        # +1 means moving down the rows (towards the last row), -1 means moving back up (towards row 0)
        # The row number alone can't tell us where to go next, because the same row is visited
        # on the way down and on the way back up
        direction = 1
        
        # Each row, joined into a single string
        rows = []
        
        # With one row there is no zigzag: every character is in the same row, so s is unchanged
        # Without this check, the direction would flip at row 0 and the row number would go negative
        if numRows == 1:
            return s
        
        # Loop through each character in s
        for i in range(len(s)):
            # Last row: place the character, then flip direction so the next step goes back up
            if row_counter == numRows-1: 
                string_list[row_counter].append(s[i])
                direction = -1
                row_counter += direction
            # First row: place the character, then set direction down so the next step goes to row 1
            elif row_counter == 0:
                string_list[row_counter].append(s[i])
                direction = 1
                row_counter += direction 
            # Any middle row: place the character and keep moving in the current direction
            else:
                string_list[row_counter].append(s[i])
                row_counter += direction
        
        # Turn each row (a list of characters) into one string, keeping the rows in top to bottom order
        for i in range(len(string_list)):
            x = "".join(string_list[i])
            rows.append(x)
            
        # Join the row strings, top row first, into the final answer
        return "".join(rows)
    
# Time complexity: O(n + r), where n is the number of characters in s and r is numRows
    # Creating string_list: r empty lists -> O(r)
    # First for loop: n iterations, O(1) work each -> O(n)
    # Second for loop: r iterations, one per row. Across all rows, every character is joined once -> O(r + n)
    # Final "".join(rows): combines r strings holding n characters in total -> O(r + n)
    # The steps run one after the other, so their costs add: O(r) + O(n) + O(r + n) + O(r + n) = O(n + r)

# Space complexity: O(n + r)
    # string_list: r lists, holding n characters in total -> O(n + r)
    # rows: r strings, holding n characters in total -> O(n + r)
    # The final joined string (n characters) is the return value
    # i, direction and row_counter are single integers -> O(1)
    # Total: O(n + r)

if __name__ == "__main__":
    sol = Solution()
    print(sol.convert(("ABC"),1))
    print(sol.convert(("PAYPALISHIRING"),3))
    print(sol.convert(("PAYPALISHIRING"),4))