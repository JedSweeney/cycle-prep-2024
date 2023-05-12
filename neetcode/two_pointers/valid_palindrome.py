# A phrase is a palindrome if, after converting all uppercase letters
# into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers 

# Given a strings s, return true if it is a palindrome, or false otherwise

import re

class Solution:
    def isPalindrome(self, s): 
        s = (''.join(filter(str.isalnum, s))).lower()
        # word = re.sub(r'[^a-zA-Z0-9]', '', s).lower() Another way to filter out non-alphanumeric characters 
        return s == s[::-1]
    
    def isPalindromeV2(self, s): 
        s = (''.join(filter(str.isalnum, s))).lower() 
        left_pointer = 0 
        right_pointer = len(s) - 1
        
        while left_pointer - right_pointer <= 1:  
            if s[left_pointer] == s[right_pointer]: 
                left_pointer += 1 
                right_pointer -= 1
            else: 
                return False
        return True 


solution = Solution()

assert solution.isPalindrome("aaa") is True 
assert solution.isPalindrome("aba") is True 
assert solution.isPalindrome("zaa") is False 
assert solution.isPalindrome("Mr. Owl ate my metal worm") is True
assert solution.isPalindrome("AABb") is False
assert solution.isPalindrome("aabBaa")
assert solution.isPalindromeV2("aaa") is True 
assert solution.isPalindromeV2("aba") is True 
assert solution.isPalindromeV2("zaa") is False 
assert solution.isPalindromeV2("Mr. O%^#$&*wl ate my m%^@#&$*(!etal worm") is True
assert solution.isPalindromeV2("AABb") is False
assert solution.isPalindromeV2("aabBaa")

print("All Tests Pass!")

