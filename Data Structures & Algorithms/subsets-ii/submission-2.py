class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        cur = []
        res = []
        nums.sort()
        def backtrack(i):
            if i >= len(nums):
                res.append(cur.copy())
                return
            cur.append(nums[i])
            backtrack(i+1)
            while i < len(nums)-1:
                if nums[i] != nums[i+1]:
                    break
                i+=1
            cur.pop()
            backtrack(i+1)

            

        backtrack(0)
        return res