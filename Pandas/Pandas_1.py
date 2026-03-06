import numpy as np
import pandas as pd

#PART 1: Creating a DataFrame from a list -> Each item becomes a new row

lst = ["this", "is", "my", "first", "pandas", "project"]

df = pd.DataFrame(lst)
print(df)

#PART 2: Now lets name the column

df_column = pd.DataFrame(lst, columns = ["column"])
print(df_column)

#PART 3
data = np.array([[1,2,3], [4,5,6], [7,8,9]])
df_np = pd.DataFrame(data, columns = ['A', 'B', 'C'])
print(df_np)