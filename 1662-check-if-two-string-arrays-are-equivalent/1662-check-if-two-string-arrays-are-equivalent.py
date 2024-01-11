class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        n=len(word1)
        m=len(word2)
        temp=''
        temp1=''
        for i in range(n):
            temp=temp+word1[i]
        for j in range(m):
            temp1=temp1+word2[j]
        if temp1==temp:
            return True
        else:
            return False

        