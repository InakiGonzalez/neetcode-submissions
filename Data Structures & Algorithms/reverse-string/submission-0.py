class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        B = 0
        E = len(s) - 1

        while B < E:
            s[B], s[E] = s[E], s[B]
            E -= 1
            B += 1
        return