from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k:int) -> List[int]:
        output_array = list()
        dictionary = defaultdict(int)
        #key: number, value: frequency of the number 
        #loop through input array
        for i in range(len(nums)):
            #dictionary[number] (which references the value) incremented
            dictionary[nums[i]] +=1
            
        #create an array of size n (worst case where there are n unique numbers)
        array = [[]for _ in range(len(nums)+1)]
        #for key in dictionary
        for i in dictionary:
            #append the number at index = frequency of number
            #array[index = frequency of number] = number
            array[dictionary[i]].append(i)
        
        #start at the last element, stop at the first element, increments of 1
        # start from last since we are grouping the k most frequent, and the number
        # at the last index is the most frequent since index = frequency so larger index = larger frequency
        for i in range(len(array)-1, -1, -1): 
            #if the array at that index is not empty
            if array[i]: 
                #loop through the array since each array could contain multiple numbers
                for num in array[i]:
                    #append the number to the output array
                    output_array.append(num)
                    #stop once we have k elements
                    if len(output_array) == k:
                        return output_array
                
# Space complexity:
#  O(n) -> largest data structure contains n elements
# Time complexity:
# O(n) -> loop through each element once
#
#
#

if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent([1,1,1,2,2,3,4],3))
    