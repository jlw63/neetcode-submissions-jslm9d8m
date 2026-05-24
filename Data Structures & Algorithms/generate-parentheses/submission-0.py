class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        cur = []
        res = []
        def backtrack(left, right):
            #base case
            if len(cur) == 2*n:
                res.append("".join(cur))
                return
            #case1
            if left >0:
                cur.append("(")
                backtrack(left - 1, right + 1)
                cur.pop()
            #case2
            if right > 0:
                cur.append(")")
                backtrack(left,right-1)
                cur.pop()
        backtrack(n, 0)

        return res

        