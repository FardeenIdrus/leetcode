from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges:list[list[int]], source: int, destination:int) -> bool:
        
        
        adjacency_list = defaultdict(list)
        
        for u,v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)

        visited_set = set()
        
    
        def dfs_recursive(node):

            if node == destination: 
                return True
            
            visited_set.add(node)

            for neighbour in adjacency_list[node]:
                if neighbour not in visited_set:
                    result = dfs_recursive(neighbour)
                    if  result:
                        return True
            
            return False

                    

        return dfs_recursive(source)
    


if __name__ == "__main__":
    sol = Solution()
    print(sol.validPath(3, [[0,1],[1,2],[2,0]], 0, 2))
    print(sol.validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))
    
# Time Complexity: O(V+E)

# Space Complexity: O(V+E)