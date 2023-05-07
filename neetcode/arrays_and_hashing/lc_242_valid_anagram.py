# 242. Valid Anagram 
# Given two strings s and t, return true if t is an anagram of s, and false otherwise. 

# Example 1: 
# Input: s = "anagram", t = "nagaram" 
# Output: True 

from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False 
        s_sorted = sorted(s) 
        t_sorted = sorted(t) 
        for s_char, t_char in zip(s_sorted, t_sorted): 
            if s_char != t_char:
                return False 
        return True
       
    # Returns the occurrences of characters in a string. 
    def get_counts(self, s): 
        # occurrences = defaultdict(int) 
        occurrences = dict() 
        for c in s: 
            # occurrences[c] += 1 
           occurrences[c] = occurrences.get(c, 0) + 1 
        return occurrences


        
    
    def isAnagramV2(self, s: str, t: str) -> bool:
        return self.get_counts(s) == self.get_counts(t) 
        
        

solution = Solution() 

assert solution.isAnagram('abc', 'xyz') is False
assert solution.isAnagram('aabbcc', 'cbabca') is True
assert solution.get_counts("boof") == {'o': 2, 'b': 1, 'f': 1} 
assert solution.isAnagramV2('abc', 'xyz') is False
assert solution.isAnagramV2('aabbcc', 'cbabca') is True

print("All Tests Passed!")
        # Make a dictionary to contain all the characters of the s string. 
        # s_characters = {} 
        # Loop through and add all of the characters in s into the dictionary 
        # for char in t: 
        #    s_characters[char] = char  
        # for char in s: 
        #    if char not in s_characters: 
        #        return False 
        # return True 


            
