class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
        # 1. Which index does this number point to?
            idx = abs(num) - 1
            
            # 2. Check if we've been to this index before
            if nums[idx] < 0:
                # If it's already negative, 'abs(num)' is our duplicate!
                return abs(num)
            
            # 3. Otherwise, mark it
            nums[idx] *= -1