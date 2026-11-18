from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        
        adjacency_list = defaultdict(list)
        for u,v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)


        visited_set = set()

        def dfs_recursive(node: int) -> bool:

            if node == destination:
                return True

            else:
                visited_set.add(node)
                for neighbour in adjacency_list[node]:
                    if neighbour not in visited_set:
                        answer = dfs_recursive(neighbour)
                        if answer:
                            return True
                        
            return False

        
        return dfs_recursive(source)

if __name__ == "__main__":
    sol = Solution()
    print(sol.validPath(3, [[0,1],[1,2],[2,0]], 0,2))
    
# Time Complexity: O(V + E), where V is the number of vertices, and E is the number of edges
    # Building the adjacency list requires visiting each ege, with 2 append operations each (2E steps in total)
    # DFS, visitng vertices : O(V). The visited set means dfs is called at most once per vertex
    # DFS, checking neighbours : O(E). Each edge [u,v] is stored twice in adj_list: v in u's list,
    # and u in v's list.
    # So adj_list holds 2E entries in total. In the worst case, dfs loops through every list once,
    # checking all 2E entries, which is O(E)
    # Total: O(E) + O(V) + O(E) = O(V + E)
    
# Space Complexity:
    # adj_list : O(V+E). V keys, and 2E entries in total across all lists
    # visited set: O(V). At most every vertex
    # Recursion stack: O(V). Worst case is a chain, where all V vertices waiting on the stack at once
    # adj_list dominates, since visited set and stack are both always covered by the O(V) part