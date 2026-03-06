import pandas as pd

class Solution:
    def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
        return employees.head(3)

if __name__ == "__main__":
    sol = Solution()
    employeeskey = {'Name': ['Bob', 'Adam', 'Jack'], 'Age': [6,7,8], 'Wage': [1000,2000,3000]}
    print(employeeskey)
    employee = pd.DataFrame(employeeskey, index = [0,1,2])
    print(employee)
    print(employee.head(2))
    
#The head function takes an integer as a parameter (first n number of rows)
    