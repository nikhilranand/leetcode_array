class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        sort=sorted(nums)
        n=len(sort)
        product_difference=sort[n-1]*sort[n-2]-sort[0]*sort[1]
        return product_difference