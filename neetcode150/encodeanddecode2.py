from typing import List


class Solution:
    def encode(self, strs:List[str]) -> str:
        
        encoded_word = ""
        for i in range(len(strs)):
            word_length = str(len(strs[i]))
            new_word = word_length + "#" + strs[i]
            encoded_word = encoded_word + new_word
        return encoded_word
    
    def decode(self, encoded_word) -> List[str]:
        
        decoded_word = list()
        tracker = 0
        while tracker!= len(encoded_word):
            j= tracker
            while encoded_word[j]!= "#":
                j+=1
            word_length = int(encoded_word[tracker:j])
            new_word = encoded_word[j+1:j+1+word_length]
            tracker = j+1+word_length
            decoded_word.append(new_word)
            
        
        return decoded_word

if __name__ == "__main__":
    sol = Solution()
    print(sol.encode(["HelloWorld","HelloWorld"]))
    print(sol.decode("10#HelloWorld10#HelloWorld"))

#Time complexity: O(n)
# O(n). Accessing each element in the list once in encode
# Nested while loop : O(n) -> Inner while loop does not revisit pass characters 

#Space complexity: O(k)
#Encode function use extra variable new_word which is of size O(k) which is the length of the longest word
# Decode function: uses two tracker variables and new_word. Trackers are just integers which take constant space
# regardless of input size so O(1)
#