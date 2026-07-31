class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            k = (left + right) // 2
            if nums[k] >target:
                right = k -1
            elif nums[k] < target:
                left = k + 1
            else:
                return k
        return -1