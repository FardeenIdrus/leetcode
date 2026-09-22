

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        
        # Initialise an empty set - Sets can only store immutable objects - int, str, bool
        num_set= set()
        
        # Iterate through each element in the input array
        for i in nums:
        # If the integer doesnt exist in the set, add the integer
            if i not in num_set:
                num_set.add(i)
        # If the integer already exists, that means a duplicate exists - return False
            else:
                return True
        
        # If no duplicate exists, the above return statement doesnt fire - and we return True
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.containsDuplicate([1,2,3,1]))
    print(sol.containsDuplicate([1,2,3,4]))
    print(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
    print(sol.containsDuplicate([3,3]))
    
# Time complexity : O(n) -> where n is the number of elements in the input array. 
# Iterate through each element in the input array once in the worst case- where no duplicate exist
# "if i not in num_set" : O(1) look up. The element in the set is passed through a hash function, producing
# a number used to pick it's bucket inside the dictionary's internal storage. Checking or inserting an element means
# directly computing the hash value and jumping to that bucket - no scanning required - O(1) on average

# Space complexity : O(n)- where n is the number of unique integers in the input array