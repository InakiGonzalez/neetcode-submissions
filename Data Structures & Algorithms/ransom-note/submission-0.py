from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_counts = Counter(ransomNote)
        m_counts = Counter(magazine)

        diff = r_counts - m_counts

        return not bool(diff)