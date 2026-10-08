from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        
        # Each pair [course, prereq] means prereq must be taken before course
        # All courses can be finished unless there is a cycle (e.g. A needs B and B needs A)
        # Approach: DFS from every course, and report False if a cycle is found
        
        # adj_list: course -> list of the courses it needs
        adj_list = defaultdict(list)
        # currently_visiting: the courses on the current DFS path, meaning courses we have started
        # checking but not finished yet. It does not mean "visited at some point"
        currently_visiting = set()
        
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)
        
        # Returns True if course can be finished, i.e. no cycle in its chain of prerequisites
        def dfs_recursive(course):
            
            # We reached a course that we are still in the middle of checking: we have looped back, so it is a cycle
            if course in currently_visiting:
                return False
            # Empty list means there is nothing left to check: it either has no prerequisites,
            # or it was already confirmed safe and emptied further down. Return True immediately
            if adj_list[course] == []:
                return True
            
            # Start checking this course: it is now on the current path
            currently_visiting.add(course)
            # If any prerequisite leads to a cycle, this course cannot be finished either
            for prereq in adj_list[course]:
                if not dfs_recursive(prereq): return False
            
            # All prerequisites returned True, so nothing reachable from this course leads back to it
            # Remove it from the current path. If it stayed in the set, reaching it again
            # through a different route would wrongly look like a cycle
            currently_visiting.remove(course)
            # Empty its list to mark it as confirmed safe, so later calls return True at the check above
            # and it is never rechecked
            adj_list[course] = []
                
            return True
            
        # The courses may not all be connected, so start a DFS from every course
        for course in range(numCourses):
            if not dfs_recursive(course):
                return False
        
        # No cycle found anywhere
        return True
    
# Time complexity: O(V+E), where V is the number of courses and E is the number of prerequisite pairs
    # Building adj_list: one pass over the E pairs, O(E)
    # A course's body runs at most once: once it finishes, adj_list[course] is emptied, so any later call on it returns True immediately
    # Across all courses, the prerequisite loops iterate E times in total
    # The calls that return immediately are at most V (from the outer loop) plus E (one per prerequisite pair), each O(1)
    # Total: O(E) + O(V) + O(E) = O(V+E)

# Space complexity: O(V+E)
    # adj_list: E prerequisite entries plus up to V keys, O(V+E)
    # currently_visiting: only the courses on the current chain, at most V
    # Recursion stack: the same chain, at most V calls deep
    # adj_list dominates, so the total is O(V+E)

if __name__ == "__main__":
    sol = Solution()
    print(sol.canFinish(2, [[1,0]]))
    print(sol.canFinish(2, [[1,0],[0,1]]))
    print(sol.canFinish(3, [[1,0],[0,2]]))