class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        current = []

        def backtrack(i):
            #basecase - when i == length of nums
            if i == len(nums):
                res.append(current.copy())
                return
            #case 1 - add current value
            current.append(nums[i])
            backtrack(i+1)
            #case 2 - (undo) pop value
            current.pop()
            #case 3 - (skip)
            backtrack(i+1)

        backtrack(0)
        return res