from collections import defaultdict
class Solution:
    def isAnagram(self, s:str, t: str) -> bool:
        
        dict_s = defaultdict(int)
        dict_t = defaultdict(int)
        
        for i in s:
            dict_s[i] +=1
        
        for i in t:
            dict_t[i] +=1 
        
        return dict_s == dict_t

if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))
    print(sol.isAnagram("rat", "car"))
    print(sol.isAnagram("a", "ab"))
    
# Time complexity : O(n + m), where n and m are the total number of characters (not unique) in string s and t
# We loop through each character in s and t - the loops touch every character regardless of repeats, 
# and each dictionary increment is O(1) average
# Comparing dict_s == dict_t works in two steps:
# 1) Python compares how many unique characters are in each dict (O(1) check) -
#    this is NOT the same as comparing len(s) and len(t). Example: s="aaa" and t="aa"
#    have different lengths, but both only contain the unique character 'a', so both
#    dicts have 1 entry each and pass this step.
# 2) If step 1 matches, Python checks each character's count one by one (O(1) per
#    character), stopping as soon as one doesn't match.
# Step 2 can run at most once per unique character, so it adds at most O(k) work,
# where k is the number of unique characters. Since k can never be more than n or m,
# the total time complexity stays O(n + m).

# Space complexity: O(n+m) where n is the number of unique characters in s, and m the number of unique characters
# in string t