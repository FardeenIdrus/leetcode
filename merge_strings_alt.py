class Solution:
    def mergeAlternatively(self, word1: str, word2: str) -> str:
        A,B = len(word1),len(word2)
        a,b = 0,0
        stringList = []
        word = 1
        while a < A and b <B:
            if word == 1:
                stringList.append(word1[a])
                a+=1
                word =2
            else:
                stringList.append(word2[b])
                b+=1
                word = 1

        while a < A:
            stringList.append(word1[a])
            a+=1
        while b < B:
            stringList.append(word2[b])
            b+=1

        return "".join(stringList)

if __name__ == "__main__":
    solution = Solution()
    print(solution.mergeAlternatively(word1 = "abc", word2 = "pqr"))
    
#Time: O(A+B)
#Space: O(A+B)