class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans=[]
        op=[]
        for j,num in enumerate(nums):
            if num == key:
                ans.append(j)
        for i in range(len(nums)):
            for j in ans:
                if abs(i-j)<=k:
                    op.append(i)
                    break
        return op
        