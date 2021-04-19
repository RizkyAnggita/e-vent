# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from pageEvent import Ui_EventWindow
from add_event import Ui_AddEvent
# import mysql.connector

# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "admin",
#     passwd = "admin",
#     database = "e_vent"
# )

class Ui_LoginWindow(QDialog):
    
    cur = []
    def __init__(self, widget, cur):
        super(Ui_LoginWindow, self).__init__()
        loadUi("login.ui", self)
        self.widget = widget
        self.widget.addWidget(self)
        # self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

        self.cur = cur
        self.setupUi(self)
        self.submit_login_btn.clicked.connect(self.loginfunction)
        self.password_txtbox.setEchoMode(QtWidgets.QLineEdit.Password)
        self.back_btn.clicked.connect(self.back)


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 500)
        Dialog.setStyleSheet("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(210, 80, 101, 61))
        self.label.setStyleSheet("font-size: 28pt;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 150, 131, 41))
        self.label_2.setStyleSheet("font-size: 20pt;")
        self.label_2.setObjectName("label_2")
        self.email_txtbox = QtWidgets.QLineEdit(Dialog)
        self.email_txtbox.setGeometry(QtCore.QRect(190, 150, 191, 31))
        self.email_txtbox.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"font-size: 20pt;")
        self.email_txtbox.setFrame(True)
        self.email_txtbox.setObjectName("email_txtbox")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 230, 111, 31))
        self.label_3.setStyleSheet("font-size: 20pt;")
        self.label_3.setObjectName("label_3")
        self.password_txtbox = QtWidgets.QLineEdit(Dialog)
        self.password_txtbox.setGeometry(QtCore.QRect(190, 230, 191, 31))
        self.password_txtbox.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"font-size:20pt;")
        self.password_txtbox.setFrame(True)
        self.password_txtbox.setObjectName("password_txtbox")
        self.submit_login_btn = QtWidgets.QPushButton(Dialog)
        self.submit_login_btn.setGeometry(QtCore.QRect(310, 350, 131, 41))
        self.submit_login_btn.setObjectName("submit_login_btn")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(200, 0, 101, 61))
        self.label_4.setStyleSheet("font-size: 32pt;")
        self.label_4.setObjectName("label_4")
        self.signup_btn = QtWidgets.QPushButton(Dialog)
        self.signup_btn.setGeometry(QtCore.QRect(300, 270, 91, 31))
        self.signup_btn.setObjectName("signup_btn")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(160, 280, 141, 16))
        self.label_5.setObjectName("label_5")
        self.back_btn = QtWidgets.QPushButton(Dialog)
        self.back_btn.setGeometry(QtCore.QRect(10, 10, 91, 31))
        self.back_btn.setObjectName("back_btn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Login"))
        self.label_2.setText(_translate("Dialog", "Email         : "))
        self.label_3.setText(_translate("Dialog", "Password : "))
        self.submit_login_btn.setText(_translate("Dialog", "Login"))
        self.label_4.setText(_translate("Dialog", "E-Vent"))
        self.signup_btn.setText(_translate("Dialog", "Daftar"))
        self.label_5.setText(_translate("Dialog", "Belum punya akun?"))
        self.back_btn.setText(_translate("Dialog", "Back"))

    def loginfunction(self):
        member = False
        penyelenggara = False
        member_id = 0
        penyelenggara_id = 0
        email = self.email_txtbox.text()
        password = self.password_txtbox.text()
        self.cur.execute(
            """SELECT email, password, member_id FROM member WHERE email='%s' AND password='%s'"""%(email, password,)
        )
        result = self.cur.fetchone()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        if(result!=None):
            member = True
            penyelenggara = False
            member_id = result[2]
            msg.setText("Login berhasil! ")
            msg.setInformativeText("Selamat Datang!")
            # GO TO Page Event and set current_logged_in
        else:
            self.cur.execute(
                """SELECT email, password, penyelenggara_id FROM penyelenggara WHERE email='%s' AND password='%s'"""%(email, password,)
            )
            resultPenyelenggara = self.cur.fetchone()
            if (resultPenyelenggara != None):
                penyelenggara = True
                member = False
                penyelenggara_id = resultPenyelenggara[2]
                msg.setText("Login berhasil! ")
                msg.setInformativeText("Selamat Datang!")
            else:

                msg.setText("Login gagal !")
                msg.setInformativeText("Silahkan cek kembali email dan password Anda")
                self.email_txtbox.clear()
                self.password_txtbox.clear()
        msg.exec_()
        # conn.close()
        if (member):
            ui = Ui_EventWindow(self.widget, member_id)
            self.widget.addWidget(ui)
            self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
        else:
            ui = Ui_AddEvent(self.widget, penyelenggara_id)
            self.widget.addWidget(ui)
            self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
        

    def back(self):
        self.widget.removeWidget(self)
        self.widget.setCurrentIndex(self.widget.currentIndex()-1)


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())
