class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        a = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        def split(word): 
            return list(word)  
        print(S)
        S = (split(S))
        print(S)
        for n in range(len(S)):
            x = sum(shifts)
            aindex = a.index(S[n])
            xaindex = x+aindex
            if xaindex>26:
                xaindex = xaindex % 26
                xaindex = xaindex
            S[n] = a[xaindex]
            shifts.remove(shifts[0])
        print(S)
        S = "".join(S)
        return S