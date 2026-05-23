class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        current = []

        def backtrack(i):
            #base case - if the values of the current array add up to target append to result
            total = sum(current)
            if total == target:
                result.append(current.copy())
                return
            if total > target:
                return
            if i > len(nums) -1 :
                return
            #case 1: we see how many of i's value can fit or is close to the target
            current.append(nums[i])
            backtrack(i)
            #case 2: undo
            current.pop()
            backtrack(i+1)
            

        backtrack(0)
        return result

        