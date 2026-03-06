import pandas as pd
from typing import List
class Solution:
    def getDataframeSize(self, players: pd.DataFrame)-> List[int]:
        return list(players.shape)

if __name__ == "__main__":
    sol = Solution()
    lst = ['Geeks', 'For', 'Geeks', 'is', 
            'portal', 'for', 'Geeks']
    
    lstdf = pd.DataFrame(lst)
    print(sol.getDataframeSize(lstdf))

    