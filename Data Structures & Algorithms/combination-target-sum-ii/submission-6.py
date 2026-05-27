class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        candidates.sort()
        def backtrack(i):
            #base case
            if sum(cur) == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or sum(cur) >target:
                return
            #check duplicate

            cur.append(candidates[i])
            backtrack(i+1)
            while i < len(candidates)-1:
                if candidates[i] != candidates[i+1]:
                    break
                i+=1
            cur.pop()
            backtrack(i+1)
        backtrack(0)
        return res