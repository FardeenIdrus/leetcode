from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:


        sorted_list = sorted(intervals, key = lambda x: x[0])
        overlap_list = []
        start_interval = sorted_list[0][0]
        end_interval = sorted_list[0][1]
        
        for i in range(len(sorted_list)-1):
            if sorted_list[i+1][0] <= end_interval:
                end_interval = max(end_interval,sorted_list[i+1][1])
            else:
                overlap_list.append([start_interval, end_interval])
                start_interval = sorted_list[i+1][0]
                end_interval =  sorted_list[i+1][1]
        overlap_list.append([start_interval, end_interval])


        return overlap_list
    
# Time complexity: O(n log n) -> The sorted function dominated O(n)
# sorted: O(n log n), for loop visits each element in the list once therefore O(n), where n is the number of elements in the Input List

# Space compleixty: O(n) - sorted_list is the additional memory used with size O(n) where n is the number of elements in the Input List
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.merge([[1,3],[2,6],[5,8]]))
    print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))
    print(sol.merge([[1,4],[4,5]]))
    # print(sol.merge([[4,7],[1,4]]))
    print(sol.merge([[1,3],[2,6],[5,8],[8,10],[15,18]]))
    print(sol.merge([[2,3],[4,5],[6,7],[8,9],[1,10]]
))
    
    