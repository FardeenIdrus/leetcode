from typing import List
import re
class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in range(len(strs)):
            encoded_string += str(len(strs[word])) + "#" + strs[word]
        return encoded_string
    
    def decode(self, s:str) -> List[str]:
        words = []
        #initialise tracker as first characther of input string
        # For example: 5#hello4#four, tracker = 5
        tracker = 0
        #loop through characters in the string
        while tracker!= len(s):
            #second tracker to get length of string
            #e.g if length of string is 10
            j = tracker
            #find the index of the next char of the length string, e.g)12
            #j would be 1
            #tracker would be 0
            while s[j] != "#":
                #j would be on index "#"
                j+=1
                #conver string "12" to 12
            string_length = int(s[tracker:j])
            #retrieve word once we find start and end of word
            word= s[j+1: j+1+string_length]
            #append word to list
            words.append(word)
            #point tracker to the start of the next length char 
            tracker = (j+1+string_length)
        return words 
            
                      
if __name__ =="__main__":
    sol = Solution()
    print(sol.encode(["hello","four"]))
    print(sol.decode("5#hello4#four"))
    
  
#Time complexity:O(n) 
#For encode as we are just looping through each word in the input List
# For decode: We have a nested while loop but the inner loop never revisits
# any characther that the outer loop has already passed so still O(n)

#Space complexity:O(n)
# Encode builds a string of roughly the size of the input list
#Decode just returns the input list
    