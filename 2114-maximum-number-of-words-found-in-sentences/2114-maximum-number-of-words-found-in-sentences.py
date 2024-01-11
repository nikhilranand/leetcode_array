class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        n=len(sentences)
        ans=[]
        for i in range(n):
            word_count = 1  # Start with 1 to account for the first word
            for char in sentences[i]:
                if char == " ":
                    word_count += 1
            ans.append(word_count)
        maximum=max(ans)
        return maximum

        

        