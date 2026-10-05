from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        
        visited = set()
        adj_list = defaultdict(list)
        
        # Create an adjacency list - the problem guarantees the graphs are undirected and unweighted
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
    
        # Recursive DFS function
        def dfs(current_vertex):
        # Add the current vertex to the set of visited vertex 
            visited.add(current_vertex)
            
        # If the current vertex is the destination vertex, a path exists from the source to the vertex -> return True
            if current_vertex == destination: 
                return True
            
            # Explore each neighbour of the current vertex
            for neighbour in adj_list[current_vertex]:
            # Check that the neighbour has not already been visited
                if neighbour not in visited:
                 # If it has not been visited, call the recursive function on the neighbour vertex
                    result = dfs(neighbour)
                    # If the recursive stack returns True, a path exists from the source to the destination vertex
                    if result:
                        return True                    
                
            return False
        
        # Call the recursive function on the source vertex
        return dfs(source)
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.validPath(3,[[0,1],[1,2],[2,0]], 0, 2))
    print(sol.validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))

# Time complexity: O(V+E), where V is the number of vertices and E is the number of edges
# Building adj_list: O(E). One iteration per edge, with 2 appends each (2E steps in total)
# DFS, visiting vertices: O(V). The visited set means dfs is called at most once per vertex
# DFS, checking neighbours: O(E). Each edge [u, v] is stored twice in adj_list: v in u's list, and u in v's list.
# So adj_list holds 2E entries in total. In the worst case, dfs loops through every list once,
# checking all 2E entries, which is O(E)
# Total: O(E) + O(V) + O(E) = O(V+E)

# Space complexity: O(V+E)
# adj_list: O(V+E). V keys, and 2E entries in total across all lists
# visited set: O(V). At most every vertex
# Recursion stack: O(V). Worst case is a chain, with all V vertices waiting on the stack at once
# adj_list dominates, since the visited set and stack are both already covered by the O(V) part