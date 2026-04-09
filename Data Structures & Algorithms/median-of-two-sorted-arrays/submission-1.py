class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        a, b = nums1, nums2
        if len(nums1) > len(nums2):
            a, b = b, a
        n = len(a)
        m = len(b)
        total_length = n + m
        half_length = (total_length + 1)//2
        l = 0
        r = n

        while l <= r:
            i = (l+r)//2
            j = half_length - i
            Aleft = a[i-1] if i > 0 else float('-inf')
            Aright = a[i] if i < n else float('inf')
            Bleft = b[j-1] if j > 0 else float('-inf')
            Bright = b[j] if j < m else float('inf')
            if Aleft <= Bright and Bleft <= Aright:
                if total_length % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright,Bright)) / 2.0
                else:
                   return max(Aleft,Bleft)
            elif Aleft > Bright:
                r = i -1
            else:
                l = i +1

