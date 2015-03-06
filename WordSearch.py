class Solution:
# @param board, a list of lists of 1 length string
# @param word, a string
# @return a boolean
    def exist(self, board, word):

        col_len, row_len = board[0].__len__, board.__len__

        for i in range(row_len):
            for j in range(col_len):
                visited = [[0 for col in range(col_len) for row in range(row_len)
                if self.helper(board, i, j, visited, -1, 0, word):
                    return True
        return False

        
    def helper(self, board, i, j, visited, last, maxlength, word):
        if maxlength == word.__len__:
            return True
        if(last != 0 and i>0) and visited[i-1][j] == 0 and (board[i-1][j] == word[maxlength]):
            visited[i-1][j] = 1
            if self.helper( board, i-1, j, visited, 0, maxlength+1, word):
                return True
            visited[i-1[j] = 0
        if(last != 1 and i<board.__len__ - 1) and visited[i+1][j] == 0 and (board[i+1][j] == word[maxlength]):
            visited[i+1][j] = 1
            if self.helper( board, i+1, j, visited, 1, maxlength+1, word):
                return True
            visited[i+1[j] = 0
        if(last != 2 and j>0) and visited[i][j-1] == 0 and (board[i][j-1] == word[maxlength]):
            visited[i][j-1] = 1
            if self.helper( board, i, j-1, visited, 2, maxlength+1, word):
                return True
            visited[i-1[j] = 0
        if(last != 3 and j<board[0].__len__ - 1) and visited[i][j+1] == 0 and (board[i][j+1] == word[maxlength]):
            visited[i][j+1] = 1
            if self.helper( board, i, j+1, visited, 3, maxlength+1, word):
                return True
            visited[i-1[j] = 0
        return False
