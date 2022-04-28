import sys
import random
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from tttgame import *

class MainWindow(QWidget):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.resize(500,500)
        self.setWindowTitle("Tic-Tac-Toe")
        self.setStyleSheet("background-color: purple;")


        self.game = Game()

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setPen(Qt.black)
        rect = event.rect()
        size = rect.size()
        qp.setPen(Qt.DashLine)
        #drawring the board:

        colsize = size.width() // 5
        rowsize = size.height() // 5

        qp.drawLine(colsize*2, rowsize, colsize*2, rowsize*4)
        qp.drawLine(colsize*3, rowsize, colsize*3, rowsize*4)
        qp.drawLine(colsize, rowsize*2, colsize*4, rowsize*2)
        qp.drawLine(colsize, rowsize*3, colsize*4, rowsize*3)

        #drawing tokens that are on the board:
        # for R - I start a loop for the lists of lists
        # for C loop, I loop tru items in one of the lists that is inside the lists of lists
        for r in range(0,3):
            for c in range(0,3):
                if self.game.board[c][r] == "X":
                    self.drawX(qp, c, r, colsize, rowsize)
                elif self.game.board[c][r] == "O":
                    self.drawO(qp, c, r, colsize, rowsize)

    def drawX(self, qp, c, r, colsize, rowsize):
        x = colsize + c*colsize
        y = rowsize + r*rowsize
        qp.setPen(Qt.white)
        colmargin = int(colsize * 0.1)
        rowmargin = int(rowsize * 0.1)
        qp.drawLine(x + colmargin, y + rowmargin, x+colsize -colmargin, y+rowsize-rowmargin)
        qp.drawLine(x+colsize-colmargin, y+rowmargin, x+colmargin, y+rowsize-rowmargin)

    def drawO(self, qp, c, r, colsize, rowsize):
        qp.setPen(Qt.black)
        x = colsize + c*colsize
        y = rowsize + r*rowsize
        colmargin = int(colsize * 0.1)
        rowmargin = int(rowsize * 0.1)
        qp.drawEllipse(x+colmargin,y+rowmargin,colsize-colmargin*2,rowsize-rowmargin*2)


    def mousePressEvent(self, event):
        size = self.size()

        colsize = size.width() // 5
        rowsize = size.height() // 5

        col = (event.x() // colsize) - 1
        row = (event.y() // rowsize) - 1
        
        if col >= 0 and col < 3 and row >= 0 and row<3:
            self.game.TakeTurn(col, row)

        #force a repaint
        self.repaint()

        winner = self.game.checkForWinner()
        if winner != ' ':
            dlg = WinnerDialog(winner)
            if dlg.exec():
                self.game.clearBoard()
        


        

class WinnerDialog(QDialog):
    def __init__(self, winner):
        super().__init__()

        self.setWindowTitle(winner + " has won!")

        qbtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(qbtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        if winner == ' ':
            lbl = QLabel("Meh, tie. New Game?")
        else:
            lbl = QLabel("Congrats! " + winner + " has won! New game?")
        self.layout.addWidget(lbl)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()