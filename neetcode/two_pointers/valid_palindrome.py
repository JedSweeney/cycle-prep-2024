# A phrase is a palindrome if, after converting all uppercase letters
# into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers 

# Given a strings s, return true if it is a palindrome, or false otherwise

import re

class Solution:
    # def isPalindrome(self, s): 
        # combined_word = (''.join(filter(str.isalnum, s))).lower()
        # word = re.sub(r'[^a-zA-Z0-9]', '', s).lower() 
        # return word == [::-1]
    
    def isPalindromeV2(self, s): 
        combined_word = (''.join(filter(str.isalnum, s))).lower() 
        left_pointer = 0 
        right_pointer = len(combined_word) - 1
        
        while abs(left_pointer - right_pointer <= 1):  
            if combined_word[left_pointer] == combined_word[right_pointer]: 
                left_pointer += 1 
                right_pointer -= 1
            else: 
                return False
        return True 


solution = Solution()

assert solution.isPalindromeV2("aaa") is True 
assert solution.isPalindromeV2("aba") is True 
assert solution.isPalindromeV2("zaa") is False 
assert solution.isPalindromeV2("Luke is a noob!") is False
assert solution.isPalindromeV2("AABb") is False
assert solution.isPalindromeV2("aabBaa")


print("All Tests Pass!")

