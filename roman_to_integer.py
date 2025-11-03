class Solution:
    def romanToInt(self, s: str) -> int:
        d= {"I":1, "V":5, "X":10, "L":50, "C":100,"D":500, "M":1000}
        
        sum = 0
        n = len(s)
        i =0 
        
        while i<n:
            #if the value of the left character is less than the right, then add the difference
            if i < n-1 and d[s[i]] < d[s[i+1]]:
                sum += d[s[i+1]] - d[s[i]]
                i+=2
            else:
                sum += d[s[i]]
                i +=1
        
        return sum
    
                
#Time : O(n) -> Iterate through the string once
#Space : O(1)  ->  Constant sized dictionary since it doesnt depend on 
#the size of the input string
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.romanToInt(s="MDCLXVI"))    
        
# ''''
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# ''''