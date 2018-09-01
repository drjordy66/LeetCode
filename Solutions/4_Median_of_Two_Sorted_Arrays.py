class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = sorted(nums1 + nums2)
        if len(merged) % 2 == 1:
            median = merged[int(len(merged)/2)]
        else:
            median = (merged[int(len(merged)/2)] + merged[int(len(merged)/2) - 1])/2
        return median
