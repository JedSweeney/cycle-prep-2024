# Contains Duplicate 
# Given and integer array nums, return true if any value appears at least twice in the array, and return false i fevery element is distinct 

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool :
        # Create a dictionary. 
        seen_values = set() 
        # Loop through the list nums to see if the value we are iterating over is already in our dictionary. 
        for n in nums: 
            if n in seen_values: 
                return True 
            # If the value has not been seen, we add it to the dictionary. 
            seen_values.add(n)
        # This list has no duplicates 
        return False
    
    def containsDuplicateV2(self, nums): 
        # Create a set to keep track of seen values. 
        seen_values = set(nums)
        # Compare the seen_values length to the length of the orignal List
        return len(seen_values) < len(nums) 
        
solution = Solution() 
assert solution.containsDuplicate([1, 2, 3, 4]) is False  
assert solution.containsDuplicate([1, 2, 2, 3, 4]) is True

assert solution.containsDuplicateV2([1, 2, 3, 4]) is False  
assert solution.containsDuplicateV2([1, 2, 2, 3, 4]) is True

print("All Tests Passed!")

