

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        # Initialise a set storing unique jewels
        jewel_set = set()
        
        # Initialise counter to track how many stones are also jewels
        stone_jewel = 0
        
        # Loop through each character in the jewel string, and add the unique jewels into the set
        for char in jewels:
            jewel_set.add(char)
        
        # Loop through each character in the stone string, and check whether it is a jewel
        for char in stones:
            if char in jewel_set:
                
        # If the stone is in the jewel set, the stone is also a jewel, so increment the counter
                stone_jewel +=1
    
        return stone_jewel
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))
    print(sol.numJewelsInStones(jewels = "z", stones = "ZZ"))

# Time complexity : O(n+m) -> Where n+m is the total number of characters in both input strings. Loop through each character in the input strings once

# Space complexity: O(n), where n is the number of unique characters in the jewel string. 
# jewel_set scales with input size; stone_jewel is a single constant integer, so the overall space complexity is dominated by jewel_set.