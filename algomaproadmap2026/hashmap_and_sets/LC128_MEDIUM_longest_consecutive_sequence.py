class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        numSet = set(nums)

        longest_sequence = 0

        for num in numSet:
            
            # If num-1 not in numSet, this means that num is the start of a sequence 
            if num-1 not in numSet:

                # Initialise the length of this new sequence to 1 (only num is currently in this new sequence)
                current_sequence_length = 1

                # The next number in the current sequence is num+1 (e.g start of sequence = 2, next_number = 3 )
                next_number = num+1

                # Iterate through numbers that are consecutive to nums, while incrementing the length of the current sequence
                while next_number in numSet:
                    # Increment the length of the current sequence since a consecutive number to the current number exists in numSet
                    current_sequence_length +=1

                    # Increment next_number so that the while loop only executes again if a element consecutive to the current element exists in nums
                    next_number +=1

                # Set the longest sequence as the maximum consecutive sequence in nums
                longest_sequence = max(longest_sequence, current_sequence_length)

        
        return longest_sequence


# Time complexity: O(n), where n is the number of elements in nums
    # Building numSet -> inserts each element of nums once, each insert is O(1) -> O(n)
    # The for loop runs once per distinct number, which is at most n iterations
        # "if num-1 not in numSet" is an O(1) lookup done once per iteration -> n * O(1) = O(n)
        # The while loop only runs when num is the start of a sequence
            # Every number belongs to exactly one sequence, so across the whole for loop the while loop visits each number at most once
            # So it runs at most n times in total across all iterations, not n times per iteration
            # Each while iteration does one O(1) lookup (next_number in numSet) -> n * O(1) = O(n)
        # max(longest_sequence, current_sequence_length) compares two numbers -> O(1), done once per sequence start, at most n times -> O(n)
    # Steps run one after the other, so costs add: O(n) + O(n) + O(n) + O(n) = O(n)

# Space complexity: O(k), where k is the number of distinct elements in nums. Worst case every number in nums is unique, so k = n
    # numSet stores k elements -> O(k)
    # longest_sequence, current_sequence_length and next_number take constant memory -> O(1)
    # Total = O(k) + O(1) = O(k)



        