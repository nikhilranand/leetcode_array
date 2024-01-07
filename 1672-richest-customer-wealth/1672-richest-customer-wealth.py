class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        n=len(accounts)
        m=len(accounts[0])
        sum=[]
        for i in range(n):
            row_sum=0
            #row_sum=sum(accounts[i])
            for j in range(m):
                row_sum += accounts[i][j]
            sum.append(row_sum)
        biggest_num=max(sum)
        return biggest_num

        