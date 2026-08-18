class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s = s + i + ";"
        return s

    def decode(self, s: str) -> List[str]:
        # strs = s.split(";")
        # return strs[:-1]
        i = 0
        strs = []
        while i < len(s):
            temp = s[i]
            while s[i] != ";":
                i += 1
                temp = temp + s[i]
            strs.append(temp[:-1])
            i += 1
            
        return strs

