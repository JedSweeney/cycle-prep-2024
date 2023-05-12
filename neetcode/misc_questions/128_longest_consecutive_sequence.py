# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence. 
# You must write an algorithm that runs in O(n) time. 

class Solution: 
    def longestConsecutive(self, nums): 
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums: 
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best

    def consecutiveSequenceVariant(self, nums): 
        nums = set(nums) 
        result = [] 
        for x in nums:
            group = []
            if x - 1 not in nums: 
                group.append(x)
                y = x + 1 
                while y in nums:
                    group.append(y)
                    y += 1 
                result.append(group)
        return result

solution = Solution() 

assert solution.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4 
assert solution.longestConsecutive([5, 6, 1, 2, 3]) == 3
assert solution.longestConsecutive([1, 1, 3, 5, 7]) == 1 
assert solution.longestConsecutive([2, 1, 3, 9, 6, 5, 8, 7]) == 5 

assert solution.consecutiveSequenceVariant([1, 2, 3, 4, 5]) == [[1, 2, 3, 4, 5]]
assert solution.consecutiveSequenceVariant([6, 5, 1, 2, 3]) == [[1, 2, 3], [5, 6]]

print("All Tests Pass!")
