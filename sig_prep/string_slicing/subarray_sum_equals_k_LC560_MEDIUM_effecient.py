from collections import defaultdict

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        
        # Key: a prefix sum (running total). Value: how many times that prefix sum has appeared so far
        # Missing keys default to 0
        prefix_sum_counts = defaultdict(int)
        # The prefix sum 0 has appeared once, before any element is added
        # This lets subarrays that start at index 0 be counted
        prefix_sum_counts[0] = 1
        
        counter = 0
        prefix_sum = 0
        
        for i in range(len(nums)):
            # Running total of nums[0] to nums[i]
            prefix_sum += nums[i]
            
            # A subarray ending at i sums to k when an earlier prefix sum equals prefix_sum - k
            # (prefix_sum minus that earlier prefix sum leaves exactly k)
            # prefix_sum_counts holds how many earlier positions had that prefix sum, so each one is a separate subarray
            if (prefix_sum - k) in prefix_sum_counts:
                counter += prefix_sum_counts[prefix_sum - k]
            
            # Record the current prefix sum after the lookup, so it only counts for later elements
            prefix_sum_counts[prefix_sum] += 1
        
        return counter


# Time complexity: O(n), where n is the number of integers in nums
    # The for loop runs n times
    # Each iteration does a constant number of dictionary lookups and updates, each O(1) on average
    # Total: n x O(1) = O(n)

# Space complexity: O(n)
    # prefix_sum_counts stores one key per distinct prefix sum
    # Worst case every prefix sum is different, giving n + 1 keys (including the starting 0), which is O(n)
    # counter, prefix_sum and i are single integers: O(1)


if __name__ == "__main__":
    sol = Solution()
    print(sol.subarraySum([1,1,1], 2))
    print(sol.subarraySum([1,2,3], 3))
    print(sol.subarraySum([1,2,3,0,5], 3))