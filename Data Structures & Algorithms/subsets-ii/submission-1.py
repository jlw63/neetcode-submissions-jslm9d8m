class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        #sort nums for duplication check
        nums.sort()
        def backtrack(i):
            #basecase - index out of bounds
            if i == len(nums):
                res.append(cur.copy())
                return
            #case 1
            cur.append(nums[i])
            backtrack(i+1)
            #case 2
            cur.pop()
            while (i+1) < len(nums) and  nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1)

        backtrack(0)
        return res
        