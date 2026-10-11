import itertools
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        row_characters = [[] for _ in range(numRows)]
        direction = 1
        current_row = 0
        last_row = numRows-1
        
        if numRows == 1:
            return s
            
        
        for i in range(len(s)):
            
            if direction == 1:
                row_characters[current_row].append(s[i])
                if current_row == last_row:
                    current_row -=1
                    direction = -1
                else:
                    current_row +=1
                
            elif direction == -1:
                row_characters[current_row].append(s[i])
                if current_row == 0:
                    current_row +=1
                    direction =1
                else:
                    current_row -=1

        
        new_string = "".join("".join(rowchar) for rowchar in row_characters)
     
        return new_string

if __name__ == "__main__":
    sol = Solution()
    print(sol.convert("PAYPALISHIRING", 3))
    print(sol.convert("PAYPALISHIRING", 4))