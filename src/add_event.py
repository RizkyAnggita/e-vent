# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_event.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox, QAbstractButton
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as connector

class Ui_AddEvent(QMainWindow):
    widget = []
    penyelenggara_id = 0

    def __init__(self, widget, penyelenggara_id, parent=None):
        super().__init__()
        self.widget = widget
        self.widget.addWidget(self)
        self.penyelenggara_id = penyelenggara_id
        # self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
        loadUi("add_event.ui", self)
        self.setupUi(self)
        self.setupDatabase()
        print("ID Penyelenggara: " , self.penyelenggara_id)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(492, 488)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(40, 20, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.namaTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.namaTextEdit.setGeometry(QtCore.QRect(40, 110, 421, 41))
        self.namaTextEdit.setObjectName("namaTextEdit")
        self.namaEventLabel = QtWidgets.QLabel(self.centralwidget)
        self.namaEventLabel.setGeometry(QtCore.QRect(60, 90, 71, 16))
        self.namaEventLabel.setObjectName("namaEventLabel")
        self.deskripsiTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.deskripsiTextEdit.setGeometry(QtCore.QRect(40, 190, 421, 41))
        self.deskripsiTextEdit.setObjectName("deskripsiTextEdit")
        self.deskripsiLabel = QtWidgets.QLabel(self.centralwidget)
        self.deskripsiLabel.setGeometry(QtCore.QRect(60, 170, 71, 16))
        self.deskripsiLabel.setObjectName("deskripsiLabel")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(40, 270, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setCalendarPopup(True)
        self.tanggalLabel = QtWidgets.QLabel(self.centralwidget)
        self.tanggalLabel.setGeometry(QtCore.QRect(60, 250, 71, 16))
        self.tanggalLabel.setObjectName("tanggalLabel")
        self.biayaLabel = QtWidgets.QLabel(self.centralwidget)
        self.biayaLabel.setGeometry(QtCore.QRect(60, 310, 71, 16))
        self.biayaLabel.setObjectName("biayaLabel")
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(40, 380, 75, 23))
        self.submitButton.setObjectName("submitButton")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(40, 330, 111, 22))
        self.spinBox.setMaximum(999999999)
        self.spinBox.setObjectName("spinBox")
        self.namaEventValidLabel = QtWidgets.QLabel(self.centralwidget)
        self.namaEventValidLabel.setGeometry(QtCore.QRect(340, 150, 121, 21))
        self.namaEventValidLabel.setObjectName("namaEventValidLabel")
        self.deskripsiValidLabel = QtWidgets.QLabel(self.centralwidget)
        self.deskripsiValidLabel.setGeometry(QtCore.QRect(340, 230, 121, 21))
        self.deskripsiValidLabel.setObjectName("deskripsiValidLabel")
        self.tanggalValidLabel = QtWidgets.QLabel(self.centralwidget)
        self.tanggalValidLabel.setGeometry(QtCore.QRect(160, 270, 121, 21))
        self.tanggalValidLabel.setObjectName("tanggalValidLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 492, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.namaTextEdit.textChanged.connect(self.checkNama)
        self.deskripsiTextEdit.textChanged.connect(self.checkDeskripsi)
        self.dateEdit.dateChanged.connect(self.checkTanggal)
        self.submitButton.clicked.connect(self.checkData)

        self.namaValid = False
        self.deskripsiValid = False
        self.tanggalValid = False

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setupDatabase(self):
        
        self.mydb = connector.connect(
            user="admin",
            password="admin",
            host="localhost",
            database="e_vent")

        self.mycursor = self.mydb.cursor()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titleLabel.setText(_translate("MainWindow", "Add New Event"))
        self.namaEventLabel.setText(_translate("MainWindow", "Nama Event"))
        self.deskripsiLabel.setText(_translate("MainWindow", "Deskripsi"))
        self.tanggalLabel.setText(_translate("MainWindow", "Tanggal"))
        self.biayaLabel.setText(_translate("MainWindow", "Biaya"))
        self.submitButton.setText(_translate("MainWindow", "Submit"))
        self.spinBox.setPrefix(_translate("MainWindow", "Rp"))
        self.namaEventValidLabel.setText(_translate("MainWindow", "Nama kosong"))
        self.deskripsiValidLabel.setText(_translate("MainWindow", "Deskripsi kosong"))
        self.tanggalValidLabel.setText(_translate("MainWindow", "Tanggal sudah lewat"))

    def checkStringLength(self, caller:QtWidgets.QPlainTextEdit, label:QtWidgets.QLabel, context: str):
        # textLength = caller.toPlainText().__len__()
        lengthCode = checkStringLength(caller.toPlainText(), 256)
        if lengthCode == 2:
            label.setText(context + " terlalu panjang")
            return False
        elif lengthCode == 0:
            label.setText(context + " kosong")
            return False
        else:
            label.setText(context + " valid")
            return True

    def checkNama(self):
        self.namaValid = self.checkStringLength(self.namaTextEdit, self.namaEventValidLabel, "Nama")

    def checkDeskripsi(self):
        self.deskripsiValid = self.checkStringLength(self.deskripsiTextEdit, self.deskripsiValidLabel, "Deskripsi")

    def checkTanggal(self):
        isDateValid = checkTanggal(self.dateEdit.date())
        if not(isDateValid):
            self.tanggalValidLabel.setText("Tanggal sudah lewat")
            self.tanggalValid = False
        else:
            self.tanggalValidLabel.setText("Tanggal valid")
            self.tanggalValid = True
        

    def checkData(self):
        if (self.namaValid and self.deskripsiValid and self.tanggalValid):
            self.showConfirmationPopup()
        else:
            self.showInvalidPopup()

    def showInvalidPopup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Invalid Data")
        msg.setText("Data yang dimasukkan tidak valid!")
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok)

        x = msg.exec_()

    def showConfirmationPopup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Confirm Data")
        msg.setText("Apakah data yang dimasukkan sudah benar?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.buttonClicked.connect(self.popupButtonClicked)

        x = msg.exec_()

    def showSuccessPopup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Data Recorded")
        msg.setText("Data telah berhasil dicatat")
        msg.setIcon(QMessageBox.NoIcon)
        msg.setStandardButtons(QMessageBox.Ok)

        x = msg.exec_()

    def popupButtonClicked(self, i:QAbstractButton):
        if (i.text() == "&Yes"):
            dataTuple = (
                self.namaTextEdit.toPlainText(), 
                self.deskripsiTextEdit.toPlainText(), 
                self.dateEdit.date().toString("yyyyMMdd"),
                str(self.spinBox.value()),
                self.penyelenggara_id
            )

            sql = "INSERT INTO event (namaEvent, deskripsi, tanggal, biaya, penyelenggara_id) VALUES (%s, %s, %s, %s, %s)"

            self.mycursor.execute(sql,dataTuple)
            self.mydb.commit()

            self.showSuccessPopup()

        elif (i.text() == "&No") :
            self.mycursor.execute("SELECT * FROM event")
            myresult = self.mycursor.fetchall()
            for x in myresult:
                print(x)


####################
# MODUL BUAT DITES #
####################
def checkStringLength(string: str, maxLength: int):
    textLength = string.__len__()
    if textLength > maxLength:
        return 2
    elif textLength == 0:
        return 0
    else:
        return 1

def checkTanggal(date: QtCore.QDate):
        if date < QtCore.QDate.currentDate():
            return False
        else:
            return True

def checkDataEvent(nama: str, deskripsi: str, tanggal: QtCore.QDate):
    return checkStringLength(nama, 256), checkStringLength(deskripsi, 256), checkTanggal(tanggal)

######################
######################

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupDatabase()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
