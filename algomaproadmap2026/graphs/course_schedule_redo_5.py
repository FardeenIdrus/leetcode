from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        
        
        adjacency_list = defaultdict(list)
        for course, prereq in prerequisites:
            adjacency_list[course].append(prereq)
            
        visited_set = set()
        currently_visiting = set()
        
        def dfs_recursive(course):
            
            if course in currently_visiting:
                return False
            if course in visited_set:
                return True
            
            currently_visiting.add(course)
            for prereq in adjacency_list[course]:
                result = dfs_recursive(prereq)
                if not result:
                    return False
            
            currently_visiting.remove(course)
            visited_set.add(course)

            return True
                
        for i in range(numCourses):
            if not dfs_recursive(i):
                return False   
        
            
        return True
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.canFinish(2, [[1,0]]))
    print(sol.canFinish(2, [[1,0],[0,1]]))