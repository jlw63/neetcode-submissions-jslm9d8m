class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        for i in nums:
            if i == val:
                continue
            else:
                nums[counter] = i
                counter += 1
        return counter
            