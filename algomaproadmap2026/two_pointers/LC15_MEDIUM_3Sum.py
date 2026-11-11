class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()
        n = len(nums)
        res = []
        
        
        for i in range(n):
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            low = i+1
            high = n-1
            target_sum = 0-nums[i]
            
            while low < high:
                sum = nums[low] + nums[high]
                
                if sum == target_sum:
                    res.append([nums[i], nums[low], nums[high]])
                    low +=1
                    while low < high and nums[low] == nums[low-1]:
                        low +=1
                    
                elif sum > target_sum:
                    high -=1
                    
                elif sum < target_sum:
                    low +=1
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([-1,0,1,2,-1,-4]))
    print(sol.threeSum([0,1,1]))
    print(sol.threeSum([0,0,0]))
    
# Time complexity: O(n^2), where n is the number of elements in nums
    # nums.sort() -> O(n log n)
    # The for loop executes at most n times
        # For each i, left_pointer only moves forward and right_pointer only moves backward, and they stop when they meet
        # So both while loops together move the pointers at most n times per i -> O(n)
        # Each comparison, arithmetic and look up operation is O(1)
    # For loop total = O(n) * O(n) = O(n^2)
    # The sort runs once before the loop, so the costs add: O(n log n) + O(n^2)
    # O(n^2) is the larger term, so the total is O(n^2)
    
# Space Complexity: O(n), where n is the number of elements in nums
    # left, right and i consume constant space -> O(1)
    # .sort() sorts nums in place, but Python's sort (Timsort) uses temporary memory while merging, up to O(n) in the worst case -> O(n)
    # Output res is not counted as it is required by the question
    # O(1) + O(n) simplifies to O(n)
    
    

    
if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([-1,0,1,2,-1,-4]))
    print(sol.threeSum([0,1,1]))
    print(sol.threeSum[0,0,0])
