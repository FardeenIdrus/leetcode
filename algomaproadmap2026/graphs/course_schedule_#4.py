from collections import defaultdict

class Solution:
    def canFinish(self, numCourse: int, prerequisites: list[list[int]]) -> bool:

        # Tracks courses on the current path being checked right now
        currently_visting = set()
        # Tracks courses already fully confirmed safe, forever
        visited = set()

        # Build the list of prerequisites for each course
        adj_list = defaultdict(list)
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)

        def dfs(course):
            # This course is already on the current path - we've looped back to it. Cycle found.
            if course in currently_visting:
                return False
            # This course was already fully checked before and confirmed safe. No need to recheck.
            if course in visited:
                return True

            # Start checking this course - mark it as part of the current path
            currently_visting.add(course)

            # Check every prerequisite this course needs
            for pre in adj_list[course]:
                # If any prerequisite leads to a cycle, this course is unsafe too
                if not dfs(pre):
                    return False

            # Every prerequisite checked out fine - this course is done and safe
            currently_visting.remove(course)
            visited.add(course)

            return True

        # Check every course, since some courses may not connect to others
        for course in range(numCourse):
            if not dfs(course):
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.canFinish(2, [[1,0]]))
    print(sol.canFinish(2, [[1,0],[0,1]]))

# Time complexity: O(V + E), where V is the number of courses and E is the number of
# prerequisite pairs. Each course is fully checked once - the "visited" check stops it
# from ever being rechecked. Each prerequisite pair is looked at once when building the
# list, and once when following it during the search.

# Space complexity: O(V + E). The prerequisite list stores all E pairs. The two sets can
# each hold up to V courses. The chain of function calls waiting to finish can also go V
# calls deep in the worst case, if one course depends on another in one long chain.