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
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                new_list.append(nums1[i])
                i += 1
            else:
                new_list.append(nums2[j])
                j += 1
        while i < len(nums1):
            new_list.append(nums1[i])
            i += 1
        while j < len(nums2):
            new_list.append(nums2[j])
            j += 1
        if len(new_list) % 2:
            return new_list[int((len(new_list) - 1) / 2)]
        else:
            return (new_list[int((len(new_list)) / 2)-1] + new_list[int((len(new_list)) / 2) ]) / 2


s = Solution()
print(s.findMedianSortedArrays([], [2,3]))
