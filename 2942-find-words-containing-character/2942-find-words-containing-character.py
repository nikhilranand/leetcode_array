class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        #n=len(words)
        ans=[]
        #for i in range(n):
        #    for j in words[i]:
        #        if x==j:
        #            #return i
        #            #return list[i]
        #            #ans=[i]
        #            ans.append(i)
        #            break
        count=0
        for word in words:
            if x in word:
                ans.append(count)
                count+=1
                
            else:
                count+=1
        return ans
        #for string in words:
        #    if x in string:
        #        ans.append()
        