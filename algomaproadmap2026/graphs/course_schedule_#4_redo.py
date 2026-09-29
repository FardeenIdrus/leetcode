from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        
        adj_list = defaultdict(list)
        visited = set()
        current_path = set()
        
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)
        
            
        
        def dfs(course):
            if course in visited:
                return True
            if course in current_path:
                return False
            
            
            current_path.add(course)
            
            for pre in adj_list[course]:
                if not dfs(course):
                    return False
                
            current_path.remove(course)
            
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
    
# Time complexity: O(V+E) where V is the number of courses and E is the number of pre-requisite pairs


# Space complexity: O(V+E) - The prerequisit list stores all E pairs. The two sets can each hold up to V courses.
# The chain of function can also go V course deep in the worse case, if one course depends on another in a long chain