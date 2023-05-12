# You are given an array prices where prices[i] is the price 
# of a given stock on the ith day. 
# You want to maximize your profit by choosing a single day to buy one stock
# and choosing a different day in the future to sell that stock 
# Return the maximum profit you can achieve from this transaction. 
# If you cannot achieve any profit, return 0. 

class Solution: 
    def maxProfit(self, prices):
        max_profit = 0
        minimum = prices[0]
        for i in range(len(prices)):
            if prices[i] < minimum: 
                minimum = prices[i] 
            elif prices[i] > minimum:
                max_profit = max(prices[i] - minimum, max_profit)
        return max_profit

solution = Solution()

assert solution.maxProfit([1, 2, 3, 4, 5]) == 4 
assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5 
assert solution.maxProfit([7, 6, 4, 3, 1]) == 0
assert solution.maxProfit([9, 1, 3]) == 2
assert solution.maxProfit([1, 40, 3]) == 39 
assert solution.maxProfit([3, 40, 1]) == 37 

print("All Tests Pass!")
