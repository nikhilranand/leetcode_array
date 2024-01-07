class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        n=len(hours)
        ans=0
        for i in hours:
            if i>=target:
                ans+=1
        return ans