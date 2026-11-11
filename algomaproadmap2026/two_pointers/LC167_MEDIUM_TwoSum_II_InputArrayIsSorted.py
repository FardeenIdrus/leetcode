class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        # Initialise pointers and index variables 
        left_pointer, right_pointer = 0, len(numbers)-1

        # Set to +1 because the array is 1-indexed
        index1, index2 = left_pointer+1, right_pointer+1

        # Execute the operations only when left_pointer is strictly less than right_pointer. If they were equal - they would be pointing to the same
        # element in numbers 
        while left_pointer < right_pointer: 
            # Compute the sum of the 2 elements 
            sum = numbers[left_pointer] + numbers[right_pointer]
            # If the sum == target, return the indices as a list
            if sum == target:
                return [index1, index2]
            
            # If the sum is less than the target, increment the left pointer so that the sum would increase
            elif sum < target:
                left_pointer +=1
                index1 +=1
            
            # If the sum is greater than the target, decrement the right pointer so that the sum would decrease
            elif sum > target:
                right_pointer -=1
                index2 -=1


# Time complexity: O(n), where n is the number of elements in numbers
    # While loop executes at most n-1 times: each iteration moves one pointer inward by 1, and the disttance between the right pointer and left pointer starts at n-1
    # Each arithmetic, comparison and assignment operation within the while loop is an O(1) operation -> O(n-1) * O(1)
    # Simplifies to O(n)

# Space Complexity: O(1)
    # left_pointer, right_pointer, index1, index2, consume constant memory


        



        