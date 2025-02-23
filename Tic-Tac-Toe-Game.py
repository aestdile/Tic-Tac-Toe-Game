





from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys 
import os

os.system("cls")


class Project4(QMainWindow):
    def __init__(asd):
        super().__init__()

        asd.setWindowTitle("Tik_Tak Game!!!")
        asd.setGeometry(100, 150, 300, 350)

        asd.we = "X"
        asd.fd = [" "] * 9

        asd.btns = []
        for i in range(9):
            btn = QPushButton("", asd)
            btn.setGeometry((i % 3) * 100, (i // 3) * 100, 100, 100)
            btn.setStyleSheet("""color: red;
                                 border-radius: 2px solid;
                                 border: 5px solid;
                                 border-color: blue;
                                 background-color: yellow;""")
            btn.clicked.connect(lambda _, a=i: asd.btn_clicked(a))
            asd.btns.append(btn)

    def btn_clicked(asd, a):
        if asd.fd[a] == " ":
            asd.fd[a] = asd.we
            asd.btns[a].setText(asd.we)
            if asd.we == "X":
                asd.we = "O"
            else:
                asd.we = "X"

        winner = asd.check_winner()
        if winner:
            asd.show_winner(winner)

    def check_winner(asd):
        ls = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  
            [0, 4, 8], [2, 4, 6]  
        ]

        for i in ls:
            if asd.fd[i[0]] == asd.fd[i[1]] == asd.fd[i[2]] != " ":
                return asd.fd[i[0]]

        if " " not in asd.fd:
            return "Draw"

        return None

    def show_winner(asd, winner):
        if winner == "Draw":
            message = "Draw  🤝🤝🤝 !!!"
        else:
            message = f"Winner --> [ {winner} ] 🥳🥳🥳 !!!"

        label = QLabel(message, asd)
        label.setGeometry(30, 300, 300, 50)
        label.setStyleSheet("font-size: 18px; font-weight: bold; color: blue;")
        label.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    we = Project4()
    we.show()
    sys.exit(app.exec())










    