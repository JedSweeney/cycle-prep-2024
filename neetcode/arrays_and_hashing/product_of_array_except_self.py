# Given an integer array nums, return an array such that answer[i] is equal to the product of all the elements 
# of nums except nums[i] 
# The product of any prefix or suffix of nums is guarenteed to fit in a 32-bit integer 
# You must write an algorithm that runs in O(n) time and without using the division operation. 

from functools import reduce

class Solution: 
    def productExceptSelf(self, nums): 
        # Used to store the ith element, which would be the one we are not using in the multiplication
        excluded_element = [] 
        # The final array that everything will be added to
        answer = [] 
        for i in range(len(nums)):
            excluded_element = nums.pop(i) 

            excluded_multiplication = reduce(lambda x, y: x * y, nums, 1)

            answer.append(excluded_multiplication) 
            nums.insert(i, excluded_element) 
        return answer
    
solution = Solution() 

assert solution.productExceptSelf([1, 2, 3, 4]) == ([24, 12, 8, 6]) 
assert solution.productExceptSelf([1, 2]) == [2, 1]

print("All Tests Pass!")
