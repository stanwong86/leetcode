import copy

class Solution:    
    def stringSum(self, l):
        l = list(filter(lambda x: x != '.', l))
        l = [int(v) for v in l]
        return sum(l)
    
    def populateMissingRow(self, board):
        for r, row in enumerate(board):
            if row.count('.') == 1:
                value = 45 - self.stringSum(row) 
                
                c = row.index('.')
                board[r][c] = str(value)
        
    def populateMissingCol(self, board):
        for c in range(9):
            column = []
            for row in board:
                column.append(row[c])
                
            if column.count('.') == 1:
                value = 45 - self.stringSum(column) 
                
                r = column.index('.')
                board[r][c] = str(value)
    
    def getGrid(self, board, r, c):
        grid = {}
        missingCount = 0
        for a in range(3):
            for b in range(3):
                value = board[r+a][c+b]
                if value == '.':
                    missingCount += 1

                if missingCount > 1:
                    return

                grid[value] = (r+a, c+b)
        return grid
    
    def populateMissing3x3Grid(self, board):
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                grid = self.getGrid(board, r, c)
                if grid:
                    # print('grid', grid)
                    values = list(grid.keys())
                    if values.count('.') == 1:
                        value = 45 - self.stringSum(values)
                        
                        r = grid['.'][0]
                        c = grid['.'][1]
                        board[r][c] = str(value)
                # print('grid', grid)
    
    def removeFromSameRow(self, board, n, ri):
        for col in board[ri]:
            if col != '.':
                if col in n:
                    ix = n.index(col)
                    n.pop(ix)
        return n

    def removeFromSameCol(self, board, n, ci):
        for row in board:
            cell = row[ci]
            if cell != '.':
                if cell in n:
                    ix = n.index(cell)
                    n.pop(ix)
        return n
    
    def getColumn(self, board, ci):
        cols = []
        for row in board:
            cols.append(row[ci])
        return cols
    
    def getSubset(self, board, r, c):
        cornerR = r // 3 * 3
        cornerC = c // 3 * 3
        
        values = []
        for a in range(3):
            for b in range(3):
                # print(cornerR+a, cornerC+b)
                value = board[cornerR+a][cornerC+b]
                if value != '.':
                    values.append(value)
        return values  
    
    def getCellPossibilities(self, board, ri, ci):
        n = [str(i+1) for i in range(9)]
        n = self.removeFromSameRow(board, n, ri)
        n = self.removeFromSameCol(board, n, ci)
        s = self.getSubset(board, ri, ci)
        n = list(filter(lambda v: v not in s, n))
        return n
    
    def findUniquesInSubset(self, board):
        for v in range(1, 10):
            # Loop of Subsets
            for i in range(0,9,3):
                for j in range(0,9,3):
                    # Loop in subsets
                    subset = {}
                    for a in range(3):
                        for b in range(3):
                            x = i+a
                            y = j+b
                            if board[x][y] == '.':
                                values = self.getCellPossibilities(board, x, y)
                                for v in values:
                                    if v not in subset:
                                        subset[v] = []

                                    subset[v].append((x,y))
                    # print('subset', (i,j), subset)
                    for v, nodes in subset.items():
                        if len(nodes) == 1:
                            board[nodes[0][0]][nodes[0][1]] = v
    
    def isUnique(self, values):
        values = list(filter(lambda x: x != '.', values))
        if len(set(values)) != len(values):
            return False
        return True

    def checkRows(self, board):
        for row in board:
            if not self.isUnique(row):
                print('row dupe', row)
                return False
        return True

    def checkColumns(self, board):
        for i in range(9):
            column = self.getColumn(board, i)
            if not self.isUnique(column):
                print('col dupe', column)
                return False
        return True

    def checkSubset(self, board):
        for i in range(0,9,3):
            for j in range(0,9,3):
                subset = self.getSubset(board, i, j)
                if not self.isUnique(subset):
                    print('subset dupe', subset)
                    return False
        return True

    def checkComplete(self, board):
        for rows in board:
            if '.' in rows:
                return False
        return True

    def checkBoard(self, board, done=False):
        if done and not self.checkComplete(board):
            print('Board missing values')
            return False

        if self.checkRows(board) and self.checkColumns(board) and self.checkSubset(board):
            if done:
                print('Board Complete')
            else:
                print('Board Ok')
            return True
        print('Board Wrong')
        return False

    def checkValidCell(self, board, ixs, value):
        for r in range(9):
            if board[r][ixs[1]] == str(value) and ixs[0] != r:
                # print((ixs), value, 'row dupe')
                return False

        for c in range(9):
            if board[ixs[0]][c] == str(value) and ixs[1] != c:
                # print((ixs), value, 'col dupe')
                return False

        subset = self.getSubset(board, ixs[0], ixs[1])
        if str(value) in subset:
            # print((ixs), value, 'subset dupe')
            return False

        return True

    def printBoard(self, board):
        for i, row in enumerate(board):
            print(f"{row[:3]} | {row[3:6]} | {row[6:9]}")
            # print(row)
            if i % 3 == 2:
                print('-'*51)
        print('*'*80)

    def autoFillIn(self, board):
        prevBoard = None
        while prevBoard != board:
            prevBoard = copy.deepcopy(board)
            self.populateMissingRow(board)
            self.populateMissingCol(board)
            self.populateMissing3x3Grid(board)
            self.findUniquesInSubset(board)

    def findEmptyCell(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    return (i, j)


    def trialAndError(self, board):
        emptyCell = self.findEmptyCell(board)
        if not emptyCell:
            return True
        else:
            x, y = emptyCell

        for n in range(1, 10):
            if self.checkValidCell(board, emptyCell, n):
                self.printBoard(board)
                board[x][y] = str(n)
                if self.trialAndError(board):
                    return True

                board[x][y] = '.'

    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        
        self.autoFillIn(board)
        self.printBoard(board)
        self.trialAndError(board)
        self.printBoard(board)
        self.checkBoard(board, done=True)


s = Solution()
# board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
s.solveSudoku(board)