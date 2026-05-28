class Solution:
    def partition(self, s: str) -> List[List[str]]:
        cur = []
        res = []
        path = []
        def backtrack(i):
            if i >= len(s):
                res.append(path.copy())
                return
            for j in range(i,len(s)):
                cur = s[i:j+1]
                if self.isPali(cur):
                    path.append(cur)
                    backtrack(j+1)
                    path.pop()
        backtrack(0)
        return res
    def isPali(self,word) -> bool:
        end = len(word) -1
        start = 0
        while start <= end and word[start] == word[end] :
            start += 1
            end -= 1
        if start > end:
            return True
        return False

