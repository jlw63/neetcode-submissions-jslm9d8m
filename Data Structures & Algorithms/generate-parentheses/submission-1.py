class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur =[]

        left = n
        right = 0
        def backtrack(left,right):
            #basecase
            if len(cur) == 2*n:
                res.append("".join(cur))
                return
            if left > 0:
                cur.append("(")
                backtrack(left-1,right+1)
                cur.pop()
            if right > 0:
                cur.append(")")
                backtrack(left,right-1)
                cur.pop()


        backtrack(left,right)
        return res