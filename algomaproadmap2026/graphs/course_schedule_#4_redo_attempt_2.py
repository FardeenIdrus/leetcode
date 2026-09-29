from collections import defaultdict

class Solution:
    def canFinish(self, numCourses:int, prerequisites: list[list[int]]) -> bool:
        
        adj_list = defaultdict(list)
        visited = set()
        currently_visiting = set()
        
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)
        
        
        def dfs(course):
            
            if course in visited:
                return True
            if course in currently_visiting:
                return False
            
            currently_visiting.add(course)
            for prereq in adj_list[course]:
                if not dfs(prereq):
                    return False
            
            currently_visiting.remove(course)
            visited.add(course)
            
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
            
            

if __name__ == "__main__":
    sol = Solution()
    print(sol.canFinish(2, [[1,0]]))
    print(sol.canFinish(2, [[1,0],[0,1]]))
    
#Time complexity: O(V+E), where V is the number of courses and E is the number of prerequisite pairs (the length of the prerequisites list)
#    Building adj_list takes one pass through all E pairs. The outer loop tries dfs() on every course, but each course's prequisites are only ever fully
#   checked once - once a course is added to visited, calling dfs() on it again hits "if course in visiteed: return True" immediately, with no rechecking
#   So across the whole run, every course is fully processed once (V), and every prerequiste pair is looked at once when it's course's loop runs (E)

# Space complexity: O(V+E)
#   adj_list stores all E prerequisite pairs. visited and currently_visting can each hold up to V courses. The chain of dfs calls waiting to finish
# can also go V calls deep in the worst case if one course depends on another in one long chain. 