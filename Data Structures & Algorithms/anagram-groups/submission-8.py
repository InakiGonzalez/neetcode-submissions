from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # go over all words
        # each word will be a dictionary(?) with key = word, value = array[26] or Counter
        # another loop subtracting ith counter from all the others
        # append if not counter to res =[]
        # return res
        # strs = ["act","pots","tops","cat","stop","hat"] 
        groups = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in groups:
                groups[key] = []
            groups[key].append(s)
        return list(groups.values())


