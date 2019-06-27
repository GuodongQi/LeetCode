class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        new_list = []
        i = 0
        j = 0
        m = len(nums1)
        n = len(nums2)
        l = m + n
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                new_list.append(nums1[i])
                i += 1
            else:
                new_list.append(nums2[j])
                j += 1
        while i < m:
            new_list.append(nums1[i])
            i += 1
        while j < n:
            new_list.append(nums2[j])
            j += 1
        if len(new_list) % 2:
            return new_list[l // 2]
        else:
            return (new_list[l // 2 - 1] + new_list[l // 2]) / 2


s = Solution()
print(s.findMedianSortedArrays([], [2, 3]))
