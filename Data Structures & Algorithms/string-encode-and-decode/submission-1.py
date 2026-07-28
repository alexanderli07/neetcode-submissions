class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "empty"
        s = ""
        for i in range(len(strs)):
            if i == len(strs) - 1:
                s = s + strs[i]
            else:
                s = s + strs[i] + "q1w2e3r4"
        print(s)
        return s


    def decode(self, s: str) -> List[str]:
        if s == "empty":
            return []
        s = s.split("q1w2e3r4")
        return s
