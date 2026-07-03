class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sd = {}
        td = {}
        for i in s:
            sd[i] = sd.get(i, 0) + 1
        for o in t:
            td[o] = td.get(o, 0) + 1
        return sd == td