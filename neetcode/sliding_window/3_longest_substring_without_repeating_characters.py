# Given a string s, find the length of the longest substring 
# without repeating characters 

class Solution: 
    def lengthOfLongestSubstring(self, s): 
        left = 0
        right = 0
        chars = set() 
        max_length = 0
        while right < len(s): 
            if s[right] not in chars:
                chars.add(s[right]) 
                right += 1
                max_length = max(max_length, right - left)
            else: 
                chars.remove(s[left])
                left += 1
        return max_length 


solution = Solution() 

assert solution.lengthOfLongestSubstring("testing") == 6
assert solution.lengthOfLongestSubstring("aabbcc") == 2
assert solution.lengthOfLongestSubstring("abcdeefghijj") == 6
assert solution.lengthOfLongestSubstring("") == 0

print("All Tests Pass!")
