class Solution:
    def isValidSudoku(self, board: 'List[List[str]]') -> bool:
        row_num = [[0] * 9 for i in range(9)]  # row_num[5][6] means 5 row has number 7 (6 + 1)
        col_num = [[0] * 9 for i in range(9)]  # col_num[5][6] means 5 col has number 7 (6 + 1)
        square_num = [[[0] * 9 for i in range(3)] for j in
                      range(3)]  # square_num[1][1][7] means row0-2 col3-5  has num 8

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                number = ord(board[r][c]) - ord('1')
                if row_num[r][number]:
                    return False
                else:
                    row_num[r][number] += 1
                if col_num[c][number]:
                    return False
                else:
                    col_num[c][number] += 1
                if square_num[r // 3][c // 3][number]:
                    return False
                else:
                    square_num[r // 3][c // 3][number] += 1

        return True

    def solveSudoku(self, board: 'List[List[str]]') -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r = 0
        c = 0
        while r < 9:
            while c < 9:
                if board[r][c] != '.':
                    c += 1
                    continue
                for num in range(9):
                    if board[r][c] == '.':
                        board[r][c] = str(num)
                    if not self.isValidSudoku(board):
                        board[r][c] = '.'
                    else:
                        c +=  1
                        break
                c += 1
            r += 1
        print(board)

s= Solution()
print(s.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))