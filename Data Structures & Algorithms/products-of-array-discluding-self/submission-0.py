class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = nums[i-1] *prefix[i-1]
        #suffix
        right_product = 1
        for i in range(len(nums) -1, -1, -1):
            prefix[i] *= right_product
            right_product *= nums[i]
        return prefix
        





        