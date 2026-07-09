class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 0
        for i in nums:
            if counter == 0:
                adopt = i
            if i == adopt:
                counter += 1
            else:
                counter -= 1
        return adopt