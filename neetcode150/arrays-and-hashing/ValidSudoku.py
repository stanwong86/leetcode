class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isArrayValid(arr):
            filtered = list(filter(lambda x: x != '.', arr))
            filtered_set = set(filtered)
            return len(filtered_set) == len(filtered)

        def isValidRows(board):
            for row in board:
                if not isArrayValid(row):
                    return False
            return True
        
        def isValidCols(board):
            for colIndex in range(len(board[0])):
                cols = []
                for rowIndex in range(len(board)):
                    cols.append(board[rowIndex][colIndex])
                if not isArrayValid(cols):
                    return False
            return True
        
        def isValidSubBox(board, row, col):
            subBox = []
            for rowIndex in range(row, row+3):
                for colIndex in range(col, col+3):
                    subBox.append(board[rowIndex][colIndex])
            return isArrayValid(subBox)

        def isValidSubBoxes(board):
            for rowIndex in range(0, 9, 3):
                for colIndex in range(0, 9, 3):
                    if not isValidSubBox(board, rowIndex, colIndex):
                        return False
            return True
        
        return isValidRows(board) and isValidCols(board) and isValidSubBoxes(board)
