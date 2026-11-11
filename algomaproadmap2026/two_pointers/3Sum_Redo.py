class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        # Sort in place so two pointers can be used: sum too small, move low up; sum too big, move high down
        nums.sort()

        # n is the length of nums
        n = len(nums)
        # List of triplets found
        res = []

        # Main idea: fix one number nums[i], then use two pointers on the numbers after it
        # to find a pair that adds up to -nums[i]. Then all three numbers sum to 0.
        for i in range(n):
            # nums is sorted, so every number from i onwards is at least nums[i].
            # If nums[i] > 0, all three numbers would be positive and cannot sum to 0, so stop.
            if nums[i] > 0:
                break
            # Skip nums[i] if it equals the previous number. The earlier i with the same value
            # already searched a bigger range that includes this one, so this can only give duplicates.
            elif i>0 and nums[i] == nums[i-1]:
                continue

            # low starts just after i, high starts at the end
            low = i+1
            high = n-1
            # The pair at low and high must add up to this
            target_sum = 0-nums[i]

            # Pointers move towards each other until they meet
            while low < high:
                sum = nums[low] + nums[high]

                if sum == target_sum:
                    # Found a triplet, record it
                    res.append([nums[i], nums[low], nums[high]])
                    # Move low up for the next pair
                    low +=1
                    # Skip repeated low values so the same triplet is not added twice
                    # (high stays: the sum is now too big, so the next pass moves it down)
                    while low < high and nums[low] == nums[low-1]:
                        low +=1

                # Sum too big: high is too large, move it down
                elif sum > target_sum:
                    high -=1

                # Sum too small: low is too small, move it up
                elif sum < target_sum:
                    low +=1
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([-1,0,1,2,-1,-4]))
    print(sol.threeSum([0,1,1]))
    print(sol.threeSum([0,0,0]))
                
# Time complexity: O(n^2), where n is the number of elements in nums
    # .sort() -> O(n log n)
    # The for loop runs at most n times, once per element, so O(n)
    # For each i, low and high move towards each other. Every pass of the while loop moves one of them inward, so together they cover at most n elements: O(n)
    # Arithmetic, appending, and look ups are O(1) operations
    # The for loop does O(n) work, n times: O(n) * O(n) * O(1) = O(n^2)
    # Total: the sort and the loop run one after the other, so costs add: O(n log n) + O(n^2) = O(n^2)

# Space complexity: O(n), where n is the number of elements in nums
    # Timsort -> O(n), since it creates a temporary list
    # i, low, high, n, target_sum and sum take constant space: O(1)
    # res is the output, so it is not counted
    # Total: O(n) + O(1) = O(n)


        
        