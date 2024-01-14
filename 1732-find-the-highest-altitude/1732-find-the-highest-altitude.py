class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        #n=len(gain)
        #ans=[0,None]*(n+1)
        #for i in range(n):
        #    temp=int(ans[i])+gain[i]
        #    ans.append(temp)
        #maximum=max(ans)
        #return maximum
        n = len(gain)
        altitude = 0  # Keep track of altitude directly
        maximum = 0

        for i in range(n):
            altitude += gain[i]
            maximum = max(maximum, altitude)  # Update maximum altitude

        return maximum

        