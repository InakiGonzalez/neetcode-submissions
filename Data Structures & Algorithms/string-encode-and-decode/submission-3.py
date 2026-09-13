class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for word in strs:
            length = str(len(word))
            out += length + "#" + word

        return out

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        i = 0
        length = ""
        while i < len(s):
            while s[i] != "#":
                length += s[i]
                i+=1
            length = int(length)
            i += 1
            res.append(s[i:i+length])
            i = i + length
            length = ""

        return res

