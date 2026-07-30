class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = len(nums1) -1
        m = m-1
        n = n-1
        while n >= 0 and m >= 0:
            if nums1[m] >= nums2[n]:
                nums1[temp] = nums1[m]
                m -= 1
                temp -= 1
            else:
                nums1[temp] =nums2[n]
                temp -= 1
                n -= 1
        if n >= 0:
            while temp >= 0:
                nums1[temp] = nums2[n]
                temp -= 1
                n -= 1






        