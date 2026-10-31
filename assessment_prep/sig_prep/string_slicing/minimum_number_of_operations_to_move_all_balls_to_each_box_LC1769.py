
class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        
        # answer[i] = total moves needed to bring every ball to box i
        answer = [0 for _ in boxes]
        
        # left: number of balls in the boxes before box i (boxes 0 to i-1)
        left = 0
        
        # Pass 1: count all the balls, and compute answer[0] directly
        # A ball at position i needs i moves to reach box 0, so answer[0] is the sum of all ball positions
        num_of_balls = 0
        for i in range(len(boxes)):
            if boxes[i] == "1":
                num_of_balls += 1
                answer[0] += i 
        
        # Pass 2: build answer[i] from answer[i-1], instead of recomputing from scratch
        # Moving the target from box i-1 to box i changes every ball's distance by exactly 1:
        #   each ball before box i ends up 1 move farther, so the total goes up by left
        #   each ball at box i or after it ends up 1 move closer, so the total goes down by right
        for i in range(1, len(boxes)):
            # The ball at box i-1 (if there is one) is now before box i, so it joins left
            if boxes[i-1] == "1":
                left += 1
            # Every ball is either before box i (left) or at/after it (right)
            right = num_of_balls - left
            answer[i] = answer[i-1] + left - right
        
        return answer
    
# Time complexity: O(n), where n is the number of characters in boxes
    # Creating answer: O(n)
    # First for loop: n iterations, O(1) work each, so O(n)
    # Second for loop: n-1 iterations, O(1) work each, so O(n-1) simplifies to O(n)
    # The three steps run one after the other, so their costs add: O(n) + O(n) + O(n) = O(n)

# Space complexity: O(1) extra space, excluding the required output list
    # left, right, num_of_balls and the loop variable i are single integers, constant in size
    # answer is O(n), but it is the required return value, so it isn't counted as extra space
    
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.minOperations("110"))
    print(sol.minOperations("001011"))