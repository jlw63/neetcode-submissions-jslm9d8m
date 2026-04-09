class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in range(len(strs)):
            sort = sorted(strs[i])
            s = "".join(sort)
            if s not in d:
                group = []
                d[s] = group
            d[s].append(strs[i])
        listofd = list(d.values())
        return listofd



        