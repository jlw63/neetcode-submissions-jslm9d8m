class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        
        def backtrack():
            #base case
            if len(cur) == len(nums):
                res.append(cur.copy())
                return

            
            for i in range(0,len(nums)):
                if nums[i] in cur:
                    continue
                cur.append(nums[i])
                backtrack()
                cur.pop()
        backtrack()
        return res

