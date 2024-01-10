class Solution:
    def sortSentence(self, s: str) -> str:
        words = []
        numbers = []
        current_word = ""

        for char in s:
          if char.isalpha():
            current_word += char
          elif char.isdigit():
            if current_word:
              words.append(current_word)
              current_word = ""
            numbers.append(char)
          else:
            # Handle other characters (e.g., punctuation) if needed
            pass
    
        if current_word:
          words.append(current_word)

        new=[None]*len(words)
        for i,word in enumerate(words):
            new[int(numbers[i])-1]=word
            #new.insert(int(numbers[i])-1,word)    
        return " ".join(new)
