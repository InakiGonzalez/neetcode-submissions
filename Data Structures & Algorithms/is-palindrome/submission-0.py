import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', s)
        print(cleaned_text)
        cleaned_text= cleaned_text.lower()
        cleaned_text = cleaned_text.replace(" ","")
        print(cleaned_text)

        r = len(cleaned_text) - 1
        l = 0
        while r >= l:
            if cleaned_text[l] != cleaned_text[r]:
                return False
            r -= 1
            l += 1
        return True