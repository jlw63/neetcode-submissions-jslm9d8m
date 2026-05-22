class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            result ^= i
        for i in range(0, len(nums)+ 1):
            result ^= i
        return result

        