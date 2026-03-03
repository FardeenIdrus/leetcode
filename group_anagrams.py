from typing import List
class Solution:
    def groupAnagrams(self, strs:List[str]) -> List[List[str]]:
        hash_map = {}
        
        for i in range(len(strs)):
            sort = tuple(sorted(strs[i]))
            if sort in hash_map:
                hash_map[sort].append(strs[i])
            else:
                hash_map[sort] =[strs[i]]
            
        return list(hash_map.values())

if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["cat", "tac", "act"]))
        
            
        