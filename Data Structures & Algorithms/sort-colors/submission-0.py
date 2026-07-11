class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = 0
        high = len(nums) - 1
        counter = 0
        while counter <= high:
            if nums[counter] == 1:
                counter += 1
                continue
            elif nums[counter] == 0:
                temp = nums[counter]
                nums[counter] = nums[low]
                nums[low] = temp
                low += 1
                counter += 1
            else:
                temp = nums[counter]
                nums[counter] = nums[high]
                nums[high] = temp
                high -= 1


        """
        Do not return anything, modify nums in-place instead.
        """
        