
class Solution:
    def merge(self, intervals : list[list[int]]) -> list[list[int]]:
        
        # In place transformation, sorting the input array by the first element in each nested array
        intervals.sort(key = lambda x: x[0])
        
        merge_list = []
        
        # Initialise the start and end tracker - to track the start and end of intervals
        start = intervals[0][0]
        end = intervals[0][1]
        
        
        # Loop through each nested array, starting from the second, since the first is already tracked above
        for i in range(1,len(intervals)):
        
            # If the next interval starts before (or exactly when) the current tracked interval ends, they overlap -
            # extend end to whichever is larger, since a fully-contained interval (e.g. [1,10] then [2,3]) must not shrink it
            if intervals[i][0] <= end:
                end = max(end, intervals[i][1])
            else:
                
                # No overlap: the interval being tracked is now finished, so save it,
                # then start tracking the new interval from scratch
                merge_list.append([start,end])
                start = intervals[i][0]
                end = intervals[i][1]
        
        # The last tracked interval is never closed off inside the loop (no further interval exists to trigger
        # the "else" branch), so it must be appended manually here
        merge_list.append([start, end ])                                     
        return  merge_list

if __name__ == "__main__":
    sol = Solution()
    print(sol.merge([[1,3],[2,6],[8,10], [15,18]]))
    print(sol.merge([[1,4],[4,5]]))
    print(sol.merge([[4,7],[1,4]]))
    print(sol.merge([[1,10],[2,3]]))
    print(sol.merge([[1,4],[0,2],[3,5]]))
    
# Time complexity : O(n log n) in the average/worst case of the sort function, where n is the number of nested arrays
# in the input array.
# The for loop time complexity is O(n) which is dominated by O(n log n) for large n. 
    
# Space complexity: O(1) - variables start and end are constant in size, and do not grow with the input array
# If including the output array, O(n), where n is the number of nested arrays in the input array - in the worst case,
# no intervals overlap