
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        
        low = 0
        high = len(nums)-1
        
        
        while low <= high:
            mid = (low+high)//2 
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid+1
            elif nums[mid] > target:
                high = mid -1

        
        return low
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.searchInsert([1,3,5,6], 5))
    print(sol.searchInsert([1,3,5,6], 2))
    print(sol.searchInsert([1,3,5,6], 7 ))
    
# Time Complexity: O(log n)
# Space Complexity: O(1)