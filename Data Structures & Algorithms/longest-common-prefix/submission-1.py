class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):        # i = column / position
            for s in strs:                   # s = each string
                if len(s) <= i  or s[i] != strs[0][i] :
                    return strs[0][:i]
            
                # two things to check here:
                #   - is s long enough to HAVE position i?
                #   - does s[i] match the reference char strs[0][i]?
                # if either fails → return strs[0][:i]
                
        return strs[0]  