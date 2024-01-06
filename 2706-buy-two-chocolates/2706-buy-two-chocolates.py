class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        ans=0
        total=prices[0]+prices[1]
        if total<=money:
            ans=money-total
        else:
            ans=money
        return ans
        