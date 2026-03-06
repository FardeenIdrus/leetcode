from typing import List
import pandas as pd

class Solution:

    def createDataFrame(student_data: List[List[int]])-> pd.DataFrame:
        student = pd.DataFrame(student_data, columns = ['student_id', "age"])    

        return student
    
#Time complexity = O(n) because Pandas needs to go through each row in the 2D list once to create the
# DataFrame, so it's O(n) where n is the number of rows or O(n*m) if you consider m columns

if __name__ ==  "__main__":
    sol = Solution()
    #print(sol.createDataFrame(3))