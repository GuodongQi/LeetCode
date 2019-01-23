class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        m = len(height)
        start = 0
        end = m - 1
        cont_most = 0
        while start < end:
            if height[start] < height[end]:
                h = height[start]
                start += 1
            else:
                h = height[end]
                end -= 1
            cont = h * (end - start +1)
            if cont_most < cont:
                cont_most = cont
        return cont_most
