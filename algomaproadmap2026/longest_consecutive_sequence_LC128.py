class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        # A set gives O(1) lookups and removes duplicate numbers
        numSet = set(nums)
        
        # Length of the longest consecutive sequence found so far
        longest_sequence = 0
        
        # Loop over the distinct numbers (looping over nums would repeat work for duplicates)
        for num in numSet:
           # Only count from the first number of a sequence: the one whose num - 1 is not in the set
          # e.g. {1, 2, 3, 4}: only 1 qualifies (0 is not in the set), while 2, 3 and 4 are skipped
            if num - 1 not in numSet:
                # The sequence so far is just num
                current_sequence = 1
                # The next number to look for
                next_number = num + 1
                # Step forward through num + 1, num + 2, ... for as long as each one is in the set
                while next_number in numSet:
                    current_sequence += 1
                    next_number += 1
                
                # Keep the longer of this sequence and the longest found so far
                longest_sequence = max(longest_sequence, current_sequence)
        
        return longest_sequence


# Time complexity: O(n), where n is the number of integers in nums
    # Building numSet: n insertions, O(1) each -> O(n)
    # The for loop visits each distinct number once. "num - 1 not in numSet" is an O(1) lookup -> O(n)
    # The while loop runs only when num is the start of a sequence
    # A sequence of length L costs L lookups: L - 1 that find the next number, and 1 that ends the sequence
    # Sequences never share numbers, so the lookups from all sequences added together are at most n
    # Example: [100, 4, 200, 1, 3, 2] has sequences [1, 2, 3, 4], [100] and [200]: 4 + 1 + 1 = 6 lookups for 6 numbers
    # Total: O(n) + O(n) + O(n) = O(n)

# Space complexity: O(n), where n is the number of integers in nums
    # numSet holds up to n distinct integers -> O(n)
    # longest_sequence, current_sequence, next_number and num are single integers -> O(1)


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestConsecutive([100,4,200,1,3,2]))
    print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
    print(sol.longestConsecutive([1,0,1,2]))
