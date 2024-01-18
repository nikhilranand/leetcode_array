class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n=len(words)
        m=len(pref)
        count=0
        for word in words:
            if word[:m]==pref:
                count+=1
        return count
        