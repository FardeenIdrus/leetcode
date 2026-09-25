from collections import defaultdict

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_dict= {}
        
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in num_dict:
                return [num_dict[remainder], i]
            num_dict[nums[i]] =i 
            
        return False
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2,7,11,15],9))
    print(sol.twoSum([3,2,4], 6))
    print(sol.twoSum([3,3],6 ))
    