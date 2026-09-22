from collections import defaultdict

class Solution:

    def dfs_recusion(self, adj_list, source_vertex, visited_set, destination_vertex):
        # Mark this vertex as visited before exploring it, so it's never processed again
        # (this is what prevents infinite loops in a graph with cycles)
        visited_set.add(source_vertex)

        # Base case: we've reached the destination via this path, so a valid path exists
        if source_vertex == destination_vertex:
            return True

        # Explore each neighbour of the current vertex
        for neighbour in adj_list[source_vertex]:
            # Only recurse into neighbours we haven't already visited
            if neighbour not in visited_set:
                # Ask recursively: "can the destination be reached starting from this neighbour?"
                result = self.dfs_recusion(adj_list, neighbour, visited_set, destination_vertex)

                # If that neighbour's path led to the destination, pass True straight back up
                # the chain of recursive calls, instead of continuing to check other neighbours
                if result:
                    return True

        # Every neighbour was checked and none led to the destination from here
        return False

    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        # Tracks every vertex visited across the whole search, shared by all recursive calls
        visited = set()

        # Build the adjacency list from the raw edge list.
        # The graph is undirected, so each edge is added in BOTH directions -
        # e.g. edge [0,1] means 0 can reach 1, AND 1 can reach 0
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        # Kick off the recursive search starting from source
        return self.dfs_recusion(adj_list, source, visited, destination)


if __name__ == "__main__":
    sol = Solution()
    print(sol.validPath(3, [[0,1],[1,2],[2,0]], 0, 2))
    print(sol.validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))

# Time complexity: O(V+E) - in the worst case, every vertex is visited exactly once,
# and every edge is examined exactly once (when checking a vertex's neighbours)

# Space complexity: O(V) - the visited set holds at most V vertices, and since this is
# recursive, the call stack can also go V calls deep in the worst case (a long chain graph)