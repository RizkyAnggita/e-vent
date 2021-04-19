# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup_member.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SignupMember(QDialog):
    widget = []
    cur = []    
    conn = []
    def __init__(self, widget, cur, conn):
        super(Ui_SignupMember, self).__init__()
        loadUi("signup_member.ui", self)
        self.widget = widget
        self.cur = cur
        self.conn = conn
        self.setupUi(self)
        self.submit_signup_btn.clicked.connect(self.signupMember)
        self.tanggal_lahir.setCalendarPopup(True)
        self.back_btn.clicked.connect(self.back)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 500)
        Dialog.setStyleSheet("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 80, 221, 61))
        self.label.setStyleSheet("font-size: 28pt;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 150, 141, 41))
        self.label_2.setStyleSheet("font-size: 20pt;")
        self.label_2.setObjectName("label_2")
        self.nama_txtbox = QtWidgets.QLineEdit(Dialog)
        self.nama_txtbox.setGeometry(QtCore.QRect(210, 150, 191, 31))
        self.nama_txtbox.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"font-size: 20pt;")
        self.nama_txtbox.setFrame(True)
        self.nama_txtbox.setObjectName("nama_txtbox")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 190, 141, 31))
        self.label_3.setStyleSheet("font-size: 20pt;")
        self.label_3.setObjectName("label_3")
        self.email_txtbox = QtWidgets.QLineEdit(Dialog)
        self.email_txtbox.setGeometry(QtCore.QRect(210, 190, 191, 31))
        self.email_txtbox.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"font-size:20pt;")
        self.email_txtbox.setFrame(True)
        self.email_txtbox.setObjectName("email_txtbox")
        self.submit_signup_btn = QtWidgets.QPushButton(Dialog)
        self.submit_signup_btn.setGeometry(QtCore.QRect(310, 330, 131, 41))
        self.submit_signup_btn.setObjectName("submit_signup_btn")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(200, 0, 101, 61))
        self.label_4.setStyleSheet("font-size: 32pt;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(70, 230, 141, 31))
        self.label_5.setStyleSheet("font-size: 20pt;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(70, 270, 141, 31))
        self.label_6.setStyleSheet("font-size: 20pt;")
        self.label_6.setObjectName("label_6")
        self.password_txtbox = QtWidgets.QLineEdit(Dialog)
        self.password_txtbox.setGeometry(QtCore.QRect(210, 270, 191, 31))
        self.password_txtbox.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"font-size:20pt;")
        self.password_txtbox.setFrame(True)
        self.password_txtbox.setObjectName("password_txtbox")
        self.tanggal_lahir = QtWidgets.QDateEdit(Dialog)
        self.tanggal_lahir.setGeometry(QtCore.QRect(210, 230, 201, 31))
        self.tanggal_lahir.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.tanggal_lahir.setDate(QtCore.QDate(1970, 7, 23))
        self.tanggal_lahir.setObjectName("tanggal_lahir")
        self.back_btn = QtWidgets.QPushButton(Dialog)
        self.back_btn.setGeometry(QtCore.QRect(10, 10, 91, 31))
        self.back_btn.setObjectName("back_btn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Sign Up Member"))
        self.label_2.setText(_translate("Dialog", "Nama              :"))
        self.label_3.setText(_translate("Dialog", "Email               :"))
        self.submit_signup_btn.setText(_translate("Dialog", "Sign Up"))
        self.label_4.setText(_translate("Dialog", "E-Vent"))
        self.label_5.setText(_translate("Dialog", "Tanggal Lahir:"))
        self.label_6.setText(_translate("Dialog", "Password       :"))
        self.back_btn.setText(_translate("Dialog", "Back"))

    def signupMember(self):
        nama = self.nama_txtbox.text()
        email = self.email_txtbox.text()
        tgl_lahir = self.tanggal_lahir.date().toString("yyyy-MM-dd")
        password = self.password_txtbox.text()
        print(tgl_lahir)
        self.cur.execute(
            """SELECT email FROM member WHERE email='%s'"""%(email,)
        )
        result = self.cur.fetchone()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        if (result==None):
            sql = "INSERT INTO member VALUES (NULL, %s, %s, %s, %s)"
            val = (nama, email, tgl_lahir, password)
            self.cur.execute(sql, val)
            self.conn.commit()
            msg.setText("Signup sukses!")
            msg.setInformativeText("Selamat bergabung"+nama+"!")
        else:
            msg.setText("Email sudah terdaftar! ")
            msg.setInformativeText("Silahkan gunakan email lain")
        msg.exec_()

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
