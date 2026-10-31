from collections import defaultdict
class Solution:
    def duplicateValue(self, array:list[int]) -> int:
        
        for num in array:
           
           absolute_value = abs(num)
           if array[absolute_value -1] < 0:
               return absolute_value
           else:
               array[absolute_value -1] *= -1
               
        return -1 
           
                 
  
if __name__ == "__main__":
    sol = Solution()
    print(sol.duplicateValue([2,1,5,2,3,3,4]))