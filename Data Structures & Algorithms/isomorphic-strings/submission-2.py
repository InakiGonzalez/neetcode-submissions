from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapS = {}
        mapT = {}

        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]
            print("c1: ",c1)
            print("c2: ",c2)

            if((c1 in mapS and mapS[c1] != c2) or (c2 in mapT and mapT[c2] != c1)):
                return False
            mapS[c1] = c2
            mapT[c2] = c1
        return True