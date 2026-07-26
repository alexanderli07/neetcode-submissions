class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for l in s:
            if l in t:
                t = t.replace(l, "", 1)
            else:
                return False
        return True