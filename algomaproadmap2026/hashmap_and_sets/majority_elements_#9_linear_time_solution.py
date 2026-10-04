
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
        # Candidate is the element believed to be the majority
        # (-1 is just a placeholder, it gets overwritten on the first pass)
        candidate = -1
        # votes: how many more times candidate has appeared than elements that differ from it,
        # counted since it became the candidate
        votes = 0
        
        for i in range(len(nums)):
            # No lead left, so the current element becomes the new candidate
            if votes == 0:
                candidate = nums[i]
                votes =1
            else:
            # The current element accessed = the candidate element, so the candidate's lead increases
                if (nums[i] == candidate):
                    votes+=1
            # The current element is different from the candidate element: so it cancels out one of its votes
                else:
                    votes -=1
    
    # A majority element always survives the cancelling, so it must be the candidate
    # The problem guarantees a majority element always exists in nums
        return candidate
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([3,2,3,3]))
    print(sol.majorityElement([2,2,1,1,1,2,2]))
    
# Time complexity: O(n), where n is the number of elements in input array nums
    # The for loop loops through each element in the input array nums
    
# Space complexity: O(1)
# The variables "candidate" and "votes" are constant in size and do not grow with the input array nums
 # No extra data structure is used 