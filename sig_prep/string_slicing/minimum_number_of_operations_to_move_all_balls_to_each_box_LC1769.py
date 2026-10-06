
class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        
        answer =[0 for _ in boxes]
        
        # left: number of balls behind box i (in boxes 0 to i-1)
        left = 0
        
        # Count the balls, and compute answer[0]: a ball at position i costs i moves to reach box 0
        num_of_balls = 0
        for i in range(len(boxes)):
            if boxes[i] == "1":
                num_of_balls +=1
                answer[0] +=i 
        
    
        
        # Build each answer from the previous one
        # Moving the target from box i-1 to box i makes each ball behind it 1 move farther (+left)
        # and each ball at or ahead of it 1 move closer (-right)
        for i in range(1, len(boxes)):
            # boxes[i-1] is now behind box i, so a ball there joins left
            if boxes[i-1] == "1":
                left += 1
            # right: balls at box i or ahead (total balls minus left)
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