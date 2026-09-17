from typing import List


class Solution:
    
    def format_output_range(self, start_range: int, end_range: int, ranges: List[str]) -> None:
        if start_range == end_range:
            ranges.append(str(start_range))
        else:
            packaged_range_string = str(start_range) + "->" + str(end_range)
            ranges.append(packaged_range_string)
            
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # Intialise output array
        ranges = []
        # Test case for an empty input array -> Should return an empty array
        if not nums:
            return []
        
        # Initialise the start of the range as the first element, as the input array is sorted
        start_range  = nums[0]
        # Initialise end of the range to the first element; it is moved if more numbers are an incremenent of the 
        # start range
        end_range = nums[0]
        
        # Loop through from the second element, to the last element, skipping the first, as we use i-1 comparisons
        # To compare the current element with the previous one. Starting the loop at index 0, would throw
        # an index out of range error for the i-1 comparison
        for i in range(1, len(nums)):
            # Check whether the current element is an increment of the previous element
            if nums[i] == nums[i-1]+1:
            # If yes, the current element is sequential, and the end of the range is updated
                end_range = nums[i]
            
            # If no, the sequence has been broken, and the end of the sequence is the previous element that
            # did not break the sequence
            else:
                end_range = nums[i-1]
                
                self.format_output_range(start_range, end_range, ranges)
                
                # Update the start range to the current element
                start_range = nums[i]
                # Update the end of the range to the current element
                end_range = nums[i]
                
        
        self.format_output_range(start_range, end_range, ranges) 

        return ranges


if __name__ == "__main__":
    sol = Solution()
    print(sol.summaryRanges([0,1,2,4,5,7]))
    print(sol.summaryRanges([0,2,3,4,6,8,9]))
    
# Time Complexity: O(n), where n is the number of elements in the input array. Each element in the input array
# is accessed

# Space complexity: O(1) if excluding the required output array. start_range, and end_range are constant in size,
# and do not grow with the input size. If including the required output array; the worst case is each element is it's
# own range. 