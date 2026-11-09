class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:

        # Set left pointer to the index of the first element
        left_pointer = 0
        # Set right pointer to the index of the last element
        right_pointer = len(nums)-1
        # Initialise output list
        result = []

        # Loop until the pointers cross (left pointer is strictly greater than the right pointer)
        while left_pointer <= right_pointer:
            # nums is sorted, so the largest square is at either end (the most negative or the most positive number)
            # If the absolute value at the left pointer is greater than the absolute value at the right pointer,
            # the left integer squared is greater than the right integer squared, so it is the largest square remaining
            if abs(nums[left_pointer]) > abs(nums[right_pointer]):
                # Append the squared left integer to the end of the result list
                result.append(nums[left_pointer]**2)
                # Move the left pointer inwards
                left_pointer +=1

            else:
                # This branch executes when the absolute value at the right pointer is greater than or equal to the absolute value at the left pointer
                # so the right integer squared is the largest square remaining
                # Append the squared right integer to the end of the result list
                result.append(nums[right_pointer]**2)
                # Move the right pointer inwards
                right_pointer -=1

        # Squares were appended from largest to smallest, so result is in descending order
        # Reverse it to get ascending order
        result.reverse()

        return result

# Time complexity: O(n), where n is the number of elements in nums
    # Each iteration of the while loop moves one pointer inwards and handles one element, so the loop runs n times
    # Each iteration does O(1) work: comparing two absolute values, squaring, append, moving a pointer
    # n iterations * O(1) = O(n)
    # result.reverse() reverses the list in place -> O(n)
    # The loop and the reverse run one after the other, so costs add: O(n) + O(n) = O(n)

# Space complexity: O(1)
    # left_pointer and right_pointer take constant memory -> O(1)
    # result holds n elements, but it is the required output, so it is not counted
    # reverse() works in place, so it uses no extra memory
    # Total = O(1)