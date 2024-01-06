class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n=len(arr)
        ans=[]
        mini=float(inf)
        for i in range(1,n):
            mini=min(mini,arr[i]-arr[i-1])
        for j in range(1,n):
            if arr[j]-arr[j-1]==mini:
                ans.append([arr[j-1],arr[j]])
                #ans.append(list(arr[j-1],arr[j])) # this is incorrect
        return ans

        