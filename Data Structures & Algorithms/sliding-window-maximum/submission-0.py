class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #deque = decrease array
        dq = deque()
        l = 0
        result = []
        for r in range(len(nums)):
            #pop smaller values
            while dq and nums[r] >= nums[dq[-1]]:
                dq.pop()
            dq.append(r)
            #if left index is greater than leftmost value in queue then pop
            if l > dq[0]:
                dq.popleft()
            if r - l + 1 >= k:
                result.append(nums[dq[0]])
                l += 1
            r += 1

        return result
        