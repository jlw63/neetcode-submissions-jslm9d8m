class Solution:
    def search(self, nums: List[int], target: int) -> int:
        target_index = -1
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l+r)//2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        pivot = l
        if target >= nums[l] and target <= nums[len(nums)-1]:
            l = pivot
            r = len(nums) - 1
            while l <= r:
                mid = (l + r)//2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid -1
                else:
                    return mid
                
        else:
            l = 0
            r = pivot -1
            while l <= r:

                mid = (l + r)//2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid -1
                else:
                    return mid
        return target_index

        