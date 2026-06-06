from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        '''
        s1_array = [0] * 26
        base = ord(a)
        window_size = len(s1)

        for c in s1:
            idx = abs(base - ord(c))
            s1_array[idx] += 1
        '''
        s1_counts = Counter(s1)
        window_size = len(s1)
        for i in range(len(s2) - window_size + 1):
            segment = s2[i: i + window_size]
            print(s2)
            print("segment: ",segment)
            seg_counts = Counter(segment)
            res= s1_counts - seg_counts
            print("res: ", res)
            if not(res):
                return True
        return False

        