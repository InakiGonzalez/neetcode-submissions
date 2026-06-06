class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for s in strs:
            alphabet = [0] * 26
            for c in s:
                alphabet[ord(c) - ord("a")] += 1
            anagram_map[tuple(alphabet)].append(s)
        return list(anagram_map.values())

        