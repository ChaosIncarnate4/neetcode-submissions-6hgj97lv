class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans, l, r = 0, 0, 1 
        while r < len(prices):
            if prices[r] <= prices[l]:
                l = r
            ans = max(ans, prices[r] - prices[l])
            r += 1
        
        return ans
