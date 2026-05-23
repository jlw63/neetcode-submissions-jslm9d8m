class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res =[]
        cur=[]
        def backtrack():
            #base case
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            for i in nums:
                if i in cur:
                    continue
                cur.append(i)
                backtrack()

                cur.pop()

        backtrack()
        return res




        