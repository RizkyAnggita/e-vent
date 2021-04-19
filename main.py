import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from pageEvent import Ui_EventWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        print("AAA")
        loadUi("main.ui", self)
        self.login_btn.clicked.connect(self.gotoLoginWindow)
        self.signup_member_btn.clicked.connect(self.gotoSignupMemberWindow)
        self.signup_penyelenggara_btn.clicked.connect(self.gotoSignupPenyelenggaraWindow)
    
    def gotoLoginWindow(self):
        loginWindow = LoginWindow()
        widget.addWidget(loginWindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoSignupMemberWindow(self):
        signupmember = SignupMemberWindow()
        widget.addWidget(signupmember)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    
    def gotoSignupPenyelenggaraWindow(self):
        signuppenyelenggara = SignupPenyelenggaraWindow()
        widget.addWidget(signuppenyelenggara)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class LoginWindow(QDialog):
    def __init__(self):
        super(LoginWindow, self).__init__()
        loadUi("login.ui", self)
        self.submit_login_btn.clicked.connect(self.loginfunction)
        self.password_txtbox.setEchoMode(QtWidgets.QLineEdit.Password)
        self.back_btn.clicked.connect(self.back)

    def loginfunction(self):
        email = self.email_txtbox.text()
        password = self.password_txtbox.text()
        cur.execute(
            """SELECT email, password FROM member WHERE email='%s' AND password='%s'"""%(email, password,)
        )
        result = cur.fetchone()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        if(result!=None):
            msg.setText("Login berhasil! ")
            msg.setInformativeText("Selamat Datang!")
            # GO TO Page Event and set current_logged_in
        else:
            msg.setText("Login gagal !")
            msg.setInformativeText("Silahkan cek kembali email dan password Anda")
            self.email_txtbox.clear()
            self.password_txtbox.clear()
        msg.exec_()
        # conn.close()
        ui = Ui_EventWindow()
        widget.addWidget(ui)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        

    def back(self):
        widget.removeWidget(self)
        widget.setCurrentIndex(widget.currentIndex()-1)
        
class SignupMemberWindow(QDialog):
    def __init__(self):
        super(SignupMemberWindow, self).__init__()
        loadUi("signup_member.ui", self)
        self.submit_signup_btn.clicked.connect(self.signupMember)
        self.tanggal_lahir.setCalendarPopup(True)
        self.back_btn.clicked.connect(self.back)


    def signupMember(self):
        nama = self.nama_txtbox.text()
        email = self.email_txtbox.text()
        tgl_lahir = self.tanggal_lahir.date().toString("yyyy-MM-dd")
        password = self.password_txtbox.text()
        print(tgl_lahir)
        cur.execute(
            """SELECT email FROM member WHERE email='%s'"""%(email,)
        )
        result = cur.fetchone()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        if (result==None):
            sql = "INSERT INTO member VALUES (NULL, %s, %s, %s, %s)"
            val = (nama, email, tgl_lahir, password)
            cur.execute(sql, val)
            conn.commit()
            msg.setText("Signup sukses!")
            msg.setInformativeText("Selamat bergabung"+nama+"!")
        else:
            msg.setText("Email sudah terdaftar! ")
            msg.setInformativeText("Silahkan gunakan email lain")
        msg.exec_()

    def back(self):
        widget.removeWidget(self)
        widget.setCurrentIndex(widget.currentIndex()-1)

class SignupPenyelenggaraWindow(QDialog):
    def __init__(self):
        super(SignupPenyelenggaraWindow, self).__init__()
        loadUi("signup_penyelenggara.ui", self)
        self.submit_signup_btn.clicked.connect(self.signupPenyelenggara)
        self.back_btn.clicked.connect(self.back)


    def signupPenyelenggara(self):
        nama = self.nama_txtbox.text()
        email = self.email_txtbox.text()
        no_telp = self.notelp_txtbox.text()
        password = self.password_txtbox.text()
        deskripsi = self.deskripsi_txtbox.text()

        cur.execute(
            """SELECT email FROM penyelenggara WHERE email='%s'"""%(email,)
        )
        result = cur.fetchone()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        if (result==None):
            sql = "INSERT INTO penyelenggara VALUES (NULL, %s, %s, %s, %s, %s)"
            val = (nama, email, no_telp, password, deskripsi)
            cur.execute(sql, val)
            conn.commit()
            msg.setText("Signup sukses!")
            msg.setInformativeText("Selamat bergabung"+nama+"!")
        else:
            msg.setText("Email sudah terdaftar! ")
            msg.setInformativeText("Silahkan gunakan email lain")
    
    def back(self):
        widget.removeWidget(self)
        widget.setCurrentIndex(widget.currentIndex()-1)

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
