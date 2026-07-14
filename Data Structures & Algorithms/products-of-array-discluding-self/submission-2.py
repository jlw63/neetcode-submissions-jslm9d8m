class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = 1, 1
        
        output = [1] *len(nums)
        for i in range(len(nums)):
            output[i] = prefix
            prefix = prefix * nums[i]
        for i in range(len(nums) - 1, -1, -1):
            output[i] = output[i] * suffix
            suffix = suffix * nums[i]
        return output 