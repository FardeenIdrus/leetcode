from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        
        # Initialise a default dict to assign 0 to missing keys
        dictionary = defaultdict(int)
        
        # Loop through each integer in the input array
        for i in range(len(nums)):
        # Check if the integer exist as a key in the dictionary
            if nums[i] not in dictionary:
        # If the key doesnt exist, default dict assigns the integer as the key, and the value as 1
                dictionary[nums[i]]+=1
            else:
            # If the integer already exists as a key in the dictionary - duplicate exists, return True
                return True
        
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.containsDuplicate([1,2,3,1]))
    print(sol.containsDuplicate([1,2,3,4]))
    print(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
    print(sol.containsDuplicate([3,3]))
    

# Time complexity: O(n), where n is the number of elements in the input array. We loop through each element in the input array once
# The "if nums[i] not in dictionary" -> O(1) look up time. 
# The key is passed through a hash function, which converts it into a number used to pick a "bucket" inside the dictionary's
# internal storage. Checking or inserting a key means computing this hash and jumping straight to that bucket
# - no scanning required which is why lookup is 0(1) on average 

# Space complexity: O(n), where n is the number of unique elements in the input array