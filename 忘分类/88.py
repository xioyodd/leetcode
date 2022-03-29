class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m+n-1
        while i >= n:
            nums1[i] = nums1[i-n]
            i-=1
        i = n
        j = 0
        k = 0
        while i < m+n and j < n:
            if nums1[i] <= nums2[j]:
                nums1[k] = nums1[i]
                i+=1
            else:
                nums1[k] = nums2[j]
                j+=1
            k+=1
        if i == m+n:
            while j<n:
                nums1[k] = nums2[j]
                j+=1
                k+=1
        