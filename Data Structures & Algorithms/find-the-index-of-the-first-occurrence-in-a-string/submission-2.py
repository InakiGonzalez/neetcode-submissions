class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        H = len(haystack)
        N = len(needle)
        for i in range(H-N + 1):
            print(haystack[i:len(needle)])
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1

        