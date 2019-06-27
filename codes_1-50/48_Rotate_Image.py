class Solution:
    def rotate(self, matrix: 'List[List[int]]') -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        m_new = [[None] * size for i in range(size)]
        mid = size // 2
        for i in range(size):
            for j in range(size):
                # m_new[-j+mid+mid][i] = matrix[i][j]
                m_new[i][j] = matrix[-j + mid + mid][i]
        return m_new


s = Solution()
print(s.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
