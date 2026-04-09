class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[j] <nums[i]:
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp
        #rearranged formula nums[i] = - (num[j]+nums[k]) 
        #target = -nums[i]
        #if current sum num[j] + nums[k] < target
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            target = -nums[i]
            while l < r:
                current_sum = nums[l] + nums[r]
                if current_sum < target:
                    l += 1
                if current_sum > target:
                    r -= 1
                if current_sum == target:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        return result
