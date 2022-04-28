class Game:
    def __init__(self):
        self.clearBoard()


    def clearBoard(self):
        #a place on the board is either "", x , or y
        self.board = [
            [' ',' ',' '],
            [' ',' ',' '],
            [' ',' ',' ']
        ]
    #is it X's turn?
        self.TurnX = True
        self.gameOver = False

    def TakeTurn(self, x, y):
        if self.board[x][y] != ' ' or self.gameOver:
            return

        if self.TurnX:
            token = 'X'
        
        else:
            token = 'O'

        #set the token in the right spot
        self.board[x][y] = token
        #next person's turn
        self.TurnX = not self.TurnX

    def checkForWinner(self):
        #check rows and columns
        self.gameOver = True
        for i in range(0,3):
            if self.board[i][0] != ' ' and self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return self.board[i][0]
            if self.board[0][i] != ' ' and self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]:
                return self.board[0][i]
        #checking for diagonals
        if self.board[0][0] != ' ' and self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        if self.board[2][0] != ' ' and self.board[2][0] == self.board[1][1] and self.board[1][1] == self.board[0][2]:
            return self.board[2][0]

        #no winner, keep playing:
        self.gameOver = False
        return ' '