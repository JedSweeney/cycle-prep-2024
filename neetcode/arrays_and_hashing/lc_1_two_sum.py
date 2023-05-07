# Two Sum 
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target
# You may assume that each input would have exactly one solution, and you may not use the same element twice 
# You can return the answer in any order 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a hashset to store all the numbers in. 
        seen = {} 
        # Add all of the numbers from nums to the hashset 
        for i in range(len(nums)): 
            complement = target - nums[i] 
            if complement in seen: 
                return [i, seen[complement]]
            seen[nums[i]] = i
        assert False, "Pair not found"


