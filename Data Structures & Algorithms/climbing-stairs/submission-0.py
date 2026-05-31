class Solution:
    def climbStairs(self, n: int, note={}) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n in note:
            return note[n]
        
        result = self.climbStairs(n-1, note) + self.climbStairs(n-2, note)
        note[n] = result
        return result
        