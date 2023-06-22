class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l,r = 0, 1
        maxProfit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else: 
                l = r
            r += 1
        return maxProfit


a  = Solution()
x = a.maxProfit([7,1,5,3,6,4])
print(x)
