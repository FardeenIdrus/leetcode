from collections import defaultdict

class Solution:
    def canFinish(self, numCourses:int, prerequisites: list[list[int]]) -> bool:
        
        unvisited = 0
        visiting = 1
        visited = 2
        adjacency_list = defaultdict(list)
        
        for course, prereq in prerequisites:
            adjacency_list[course].append(prereq)
            
            
        states = [unvisited] * numCourses
        
        def dfs_recursive(course: int) -> bool:
            if states[course] == visited:
                return True
            elif states[course] == visiting:
                return False
            
            
            states[course] = visiting
            
            for prereq in adjacency_list[course]:
                result = dfs_recursive(prereq)
                if not result:
                    return False
            
            states[course] = visited
            return True
        
        for i in range(numCourses):
            if not dfs_recursive(i):
                return False
            
        return  True 
    
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.canFinish(2, [[1,0]]))
    print(sol.canFinish(2, [[1,0],[0,1]]))
    print(sol.canFinish(5, [[0,1], [2,3], [3,4], [2,1], [4,2]]))