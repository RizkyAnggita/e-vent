import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from pageEvent import Ui_EventWindow
from login import Ui_LoginWindow
from signup_member import Ui_SignupMember
from signup_penyelenggara import Ui_SignupPenyelenggara

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        print("AAA")
        loadUi("main.ui", self)
        self.login_btn.clicked.connect(self.gotoLoginWindow)
        self.signup_member_btn.clicked.connect(self.gotoSignupMemberWindow)
        self.signup_penyelenggara_btn.clicked.connect(self.gotoSignupPenyelenggaraWindow)
    
    def gotoLoginWindow(self):
        # loginWindow = LoginWindow()
        loginWindow = Ui_LoginWindow(widget, cur)
        widget.addWidget(loginWindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoSignupMemberWindow(self):
        # signupmember = SignupMemberWindow()
        signupMember = Ui_SignupMember(widget, cur, conn)
        widget.addWidget(signupMember)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    
    def gotoSignupPenyelenggaraWindow(self):
        # signuppenyelenggara = SignupPenyelenggaraWindow()
        signuppenyelenggara = Ui_SignupPenyelenggara(widget, cur, conn)

        widget.addWidget(signuppenyelenggara)
        widget.setCurrentIndex(widget.currentIndex() + 1)

import mysql.connector as database
conn = database.connect(
    user="admin",
    password="admin",
    host="localhost",
    database="e_vent")

cur = conn.cursor()
print("SUKSES")
app = QApplication(sys.argv)
mainWindow = MainWindow()

widget = QtWidgets.QStackedWidget()
widget.addWidget(mainWindow)
widget.setFixedWidth(1000)
widget.setFixedHeight(800)
widget.show()

sys.exit(app.exec_())
conn.close()
