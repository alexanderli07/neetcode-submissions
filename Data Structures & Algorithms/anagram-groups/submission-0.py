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

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = []
        for i in range(len(strs)):
            temp = []
            if all(strs[i] not in row for row in final):
                for j in range(i + 1, len(strs)):
                    if self.isAnagram(strs[i], strs[j]):
                        temp.append(strs[j])
                temp.append(strs[i])
                final.append(temp)
                    

        return final
