# board: [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if board == None or len(board) == 0 or board[0] == None or len(board[0]) == 0:
            return False
        self.rows = len(board)
        self.cols = len(board[0])
        for index  in range(self.rows) :
            if not self.check_rows(board, index):
                return False
        print "A1"
        for index in range(self.cols):
            if not self.check_cols(board, index):
                return False
        print "A2"
        for row in range(self.rows / 3):
            for col in range(self.cols / 3):
                if not self.check_square(board, row, col):
                    print row, col
                    return False
        print "A3"
        return True

    def check_rows(self, board, i):
        visited = [0] * 10;
        #ERROR1
        #int object is not iterable
        #for col in self.cols:
        for col in range(self.cols):
            if board[i][col] == '.':
                continue
            elif not board[i][col].isdigit() or ord(board[i][col]) - ord('0') > 9 or ord(board[i][col]) - ord('0') < 0:
                return False
            elif visited[ord(board[i][col]) - ord('0')] != 0:
                return False
            else :
                visited[ord(board[i][col]) - ord('0')] = 1
        return True

    def check_cols(self, board, i):
        visited = [0] * 10;
        for row in range(self.rows):
            if board[row][i] == '.':
                continue
            elif not board[row][i].isdigit() or ord(board[row][i]) - ord('0') > 9 or ord(board[row][i]) - ord('0') < 0:
                return False
            elif visited[ord(board[row][i]) - ord('0')] != 0 :
                return False
            else :
                visited[ord(board[row][i]) - ord('0')] = 1
        return True

    def check_square(self, board, i, j):
        visited = [0] * 10
        for x in range(0, 3):
            for y in range(0, 3):
                #ERROR2:
                #this should multiply by a coefficient of 3
                #if board[3 * i + x][3 * j + y] == '.':
                if board[3 * i + x][3 * j + y] == '.':
                    continue
                elif not board[3 * i + x][3 * j + y].isdigit() or \
                    ord(board[3 * i + x][3 * j + y]) - ord('0') > 9 or \
                    ord(board[3 * i + x][3 * j + y]) - ord('0') < 0:
                    return False
                elif visited[ord(board[3 * i + x][3 * j + y])- ord('0')] != 0:
                    return False
                else :
                    visited[ord(board[3 * i + x][3 * j + y])- ord('0')] = 1
        return True
