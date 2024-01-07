class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n=len(candies)
        ans=[]
        maximum=max(candies)
        for i in range(n):
            temp=candies[i]+extraCandies
            #for j in range(n):
                #if temp>=candies[j] and j!=i:
                    #ans.append(True)
                    ##ans=[True]
                #elif temp<candies[j] and j!=i:
                    #ans.append(False)
                    ##ans=[False]
            
            if temp>=maximum:
                ans.append(True)
            else:
                ans.append(False)
            temp=0
        return ans



        