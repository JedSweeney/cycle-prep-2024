# Given an array of strings strs, group the anagrams together. You can return the answer in any order. 

from typing import List
from collections import Counter 
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Key: Count dictionary represnting the occurences of characters in a word 
        # Value: a list of words that are anagrams of eachother. 
        words = defaultdict(list)

        for s in strs: 
            count = [0] * 26 

            for c in s: 
                count[ord(c) - ord("a")] += 1 
                
            words[tuple(count)].append(s) 

        return words.values()            




solution = Solution() 

assert solution.groupAnagrams(["abc", "cab", "bbb"]) == [["abc", "cab"], ["bbb"]] 


