class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[]
        ans = [nums[i] for i in range(n)]
        ans =ans*2
        return ans