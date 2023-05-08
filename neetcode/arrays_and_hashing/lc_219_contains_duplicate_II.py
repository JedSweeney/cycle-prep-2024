# Given an integer array nums and an integer k, return true 
# if there are two distinct indicies i and j in the array such that 
# nums[i] == nums[j] and abs(i - j) <= k

class Solution: 
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool: 
        # Make a dictionary to store all of the seen values. 
        seen = dict() 
        for i in range(len(nums)): 
            if nums[i] in seen and abs(i - seen[nums[i]]) <= k: 
                return True 
            seen[nums[i]] = i 
        return False 

s = Solution()
s.containsNearbyDuplicate([1, 2, 3, 4], 4) is False
s.containsNearbyDuplicate([1, 2, 3, 1], 3) is True 
s.containsNearbyDuplicate([1, 0, 1, 1], 1) is True
s.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) is True

print("All Tests Pass!")

