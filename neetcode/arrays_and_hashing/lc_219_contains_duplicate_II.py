# Given an integer array nums and an integer k, return true 
# if there are two distinct indicies i and j in the array such that 
# nums[i] == nums[j] and abs(i - j) <= k

class Solution: 
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool: 
        # Make a hashset to store all of the seen values. 
        hashset = {}
        # Iterate through the elements of nums 
        for i in range(len(nums)): 
            # Check to see if the ith element in nums is alredy seen 
            # if that is the case we have a duplicate 
            # check to see if the 
            # abs(ith index - keyvalue stored in )
            if nums[i] in hashset and abs(i - hashset[nums[i]]) <= k: 
                return True 
            hashset[nums[i]] = i 
        return False 

def testContainsDuplicatesII(): 
    s = Solution() 
    test1 = s.containsNearbyDuplicate([1, 2, 3, 4], 4)
    test2 = s.containsNearbyDuplicate([1, 2, 3, 1], 3)
    test3 = s.containsNearbyDuplicate([1, 0, 1, 1], 1)
    test4 = s.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2)
    print(test1)
    print(test2)
    print(test3)
    print(test4)

testContainsDuplicatesII() 

