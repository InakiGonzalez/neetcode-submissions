from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = defaultdict(list)
        res = []
        for w in strs:
            sorted_w = sorted(w)
            sorted_w = "".join(sorted_w)
            groups[sorted_w].append(w)
        for val in groups.values():
            res.append(val)
        return res
