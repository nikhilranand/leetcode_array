class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        rows=int(s[-1])
        ans=[]
        letters = [chr(code) for code in range(ord(s[0]), ord(s[3]) + 1)]
        for char in letters:
            for i in range(int(s[1]),rows+1):
                temp=char+str(i)
                ans.append(temp)
                temp=''
        return ans
                        

        