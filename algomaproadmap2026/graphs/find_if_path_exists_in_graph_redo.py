from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        
        def dfs_recursive(source_vertex: int):
            visited_vertex.add(source_vertex)
            
            if source_vertex == destination:
                return True
            
            result = False
            for neighbour in adj_list[source_vertex]:
                if neighbour not in visited_vertex:
                    result = dfs_recursive(neighbour)
                    if result:
                        return True

            return False
        
        
        visited_vertex = set()
        
        adj_list = defaultdict(list)
        
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        
        return dfs_recursive(source)
        
        
    
    


if __name__ == "__main__":
    sol = Solution()
    print(sol.validPath(3,[[0,1],[1,2],[2,0]], 0, 2))
    print(sol.validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))