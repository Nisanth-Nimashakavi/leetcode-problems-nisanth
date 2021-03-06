class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.split()
        print(text)
        text = sorted(text, key=len)
        print(text)
        text  = ' '.join(text)
        text = text.lower()
        text = text.capitalize() 
        return text
        
        
        