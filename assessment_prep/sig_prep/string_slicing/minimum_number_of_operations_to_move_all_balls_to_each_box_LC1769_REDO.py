

class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        
        answer = [0 for _  in boxes]
        
        
        # Directly compute the answer for the first box - since the number of operations is simply equal
        # to the boxes distance to other balls
        num_balls = 0  
        left = 0
        right = 0       
        for i in range(len(boxes)):
            if boxes[i] == "1":
                answer[0] +=i
                num_balls +=1
                

        for i in range(1, len(boxes)):
            if boxes[i-1] == "1":
                left +=1
            
            right = num_balls - left
            answer[i] = answer[i-1] + (left- right)
                
            
    
        return answer
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.minOperations("110"))
    print(sol.minOperations("001011"))