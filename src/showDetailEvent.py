# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'showDetailEvent.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as connector

####################################### G U I ##############################################
class Ui_DetailEventWindow(QMainWindow):

    widget = []
    idEvent = 0
    # cur = []    
    # conn = []
    def __init__(self, widget, idEvent, member_id):
        super(Ui_DetailEventWindow, self).__init__()
        loadUi("showDetailEvent.ui", self)
        self.widget = widget
        self.widget.addWidget(self)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
        self.member_id = member_id

        self.idEvent = idEvent
        self.setupDatabase()
        # self.cur  = cur
        # self.conn = conn
        self.setupUi(self)
        self.showDetail()

    def setupUi(self, DetailEventWindow):
        DetailEventWindow.setObjectName("DetailEventWindow")
        DetailEventWindow.resize(885, 686)
        DetailEventWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(DetailEventWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 170, 611, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textDeskripsiEvent = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textDeskripsiEvent.setReadOnly(True)
        self.textDeskripsiEvent.setObjectName("textDeskripsiEvent")
        self.verticalLayout.addWidget(self.textDeskripsiEvent)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 70, 611, 89))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.namaEventLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.namaEventLabel.setFont(font)
        self.namaEventLabel.setStyleSheet("border: 3px solid black;")
        self.namaEventLabel.setObjectName("namaEventLabel")
        self.verticalLayout_2.addWidget(self.namaEventLabel)

        self.daftarButton = QtWidgets.QPushButton(self.centralwidget)
        self.daftarButton.setGeometry(QtCore.QRect(30, 560, 101, 41))
        self.daftarButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.daftarButton.setObjectName("daftarButton")
        self.daftarButton.clicked.connect(self.daftarButtonClick)

        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(10, 10, 93, 28))
        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton.setObjectName("backButton")
        self.backButton.clicked.connect(self.back)
        
        # self.testButton = QtWidgets.QPushButton(self.centralwidget)
        # self.testButton.setGeometry(QtCore.QRect(660, 10, 93, 28))
        # self.testButton.setObjectName("testButton")
        # self.testButton.clicked.connect(self.testButtonClick)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 460, 361, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.dateLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.dateLabel.setStyleSheet("border:1px solid black;")
        self.dateLabel.setText("")
        self.dateLabel.setObjectName("dateLabel")
        self.horizontalLayout.addWidget(self.dateLabel)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 510, 361, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.biayaLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.biayaLabel.setStyleSheet("border: 1px solid black;")
        self.biayaLabel.setText("")
        self.biayaLabel.setObjectName("biayaLabel")
        self.horizontalLayout_2.addWidget(self.biayaLabel)
        DetailEventWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DetailEventWindow)
        self.statusbar.setObjectName("statusbar")
        DetailEventWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DetailEventWindow)
        QtCore.QMetaObject.connectSlotsByName(DetailEventWindow)

    def retranslateUi(self, DetailEventWindow):
        _translate = QtCore.QCoreApplication.translate
        DetailEventWindow.setWindowTitle(_translate("DetailEventWindow", "MainWindow"))
        self.namaEventLabel.setText(_translate("DetailEventWindow", "test"))
        self.daftarButton.setText(_translate("DetailEventWindow", "Daftar"))
        self.backButton.setText(_translate("DetailEventWindow", "Back"))
        self.testButton.setText(_translate("DetailEventWindow", "test"))
        self.label_2.setText(_translate("DetailEventWindow", "Tanggal :"))
        self.label_3.setText(_translate("DetailEventWindow", "Biaya :"))

    def setupDatabase(self):
        
        self.mydb = connector.connect(
            user="admin",
            password="admin",
            host="localhost",
            database="e_vent")
        self.mycursor = self.mydb.cursor()

    def showDetail(self):
        self.mycursor.execute(
            """SELECT * FROM event WHERE event_id='%d'"""%(self.idEvent,)
        )
        self.namaEventLabel.setText("Tested")
        result = self.mycursor.fetchone()
        print(result[1])

        self.namaEventLabel.setText(str(result[1]))
        self.textDeskripsiEvent.setText(str(result[2]))
        self.dateLabel.setText(str(result[3]))
        self.biayaLabel.setText(str(result[4]))

    # def testButtonClick(self):

    #     self.mycursor.execute(
    #         """SELECT * FROM event WHERE event_id='%d'"""%(self.idEvent,)
    #     )
    #     self.namaEventLabel.setText("Tested")
    #     result = self.mycursor.fetchone()
    #     print(result[1])

    #     self.namaEventLabel.setText(str(result[1]))
    #     self.deskripsiEventLabel.setText(str(result[2]))
    #     self.dateLabel.setText(str(result[3]))
    #     self.biayaLabel.setText(str(result[4]))

    def daftarButtonClick(self):
        # cekKeterdaftaran event
        check = "SELECT * FROM member_event WHERE member_id={} and event_id={}".format(self.member_id, self.idEvent)
        self.mycursor.execute(check)
        result = self.mycursor.fetchone()
        if(result != None):
            warn = QMessageBox()
            warn.setWindowTitle("Message")
            warn.setText("Anda sudah mendaftar event ini")
            warn.exec_()
            return;
        
        # cek keyakinan
        ques = QMessageBox()
        ques.setWindowTitle("Message")
        ques.setIcon(QMessageBox.Question)
        ques.setText("Apakah anda yakin ingin mendaftar event ini?")
        ques.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        ques.setDefaultButton(QMessageBox.Yes)
        ques.buttonClicked.connect(self.pop_up_button_daftar)
        ques.exec_()


        # jika berbayar ke page bayar dulu
    def pop_up_button_daftar(self, i):
        if i.text() == "&No" :
            # do nothing
            pass
            
        if i.text() == "&Yes":
            if int(self.biayaLabel.text()) == 0:
                try:
                    sql = "INSERT INTO member_event VALUES (%s, %s)"
                    self.mycursor.execute(sql, (self.member_id, self.idEvent))
                    self.mydb.commit()
                except:
                    error = QMessageBox()
                    error.setText("Pendaftara gagal")
                    error.setIcon(QMessageBox.Critical)
                    pass

                message = QMessageBox()
                message.setWindowTitle("Message")
                message.setText("Pendaftaran berhasil")
                message.exec_()
            else: # biaya tidak gratis
                ### MASIH BELUM DIIMPLEMENTASIKAN DB NYA ###
                sql = "SELECT penyelenggara_id FROM event where event_id={}".format(self.idEvent)
                self.mycursor.execute(sql)
                id_penyelenggara = self.mycursor.fetchone()
                sql = "SELECT * FROM penyelenggara WHERE penyelenggara_id={}".format(int(id_penyelenggara[0]))
                self.mycursor.execute(sql)
                penyelenggara = self.mycursor.fetchone()
                ##########################################

                bayar = QMessageBox()
                bayar.setWindowTitle("Pembayaran")
                bayar.setText("Event memerlukan biaya pendaftaran")
                infodetail = "Nama Penyelenggara \t: {}\nInfo Kontak \t : {}".format(penyelenggara[1], penyelenggara[2])
                bayar.setInformativeText("Silahkan membayar biaya pendaftaran dan mengonfirmasikannya ke penyelenggara event pada detail dibawah")
                bayar.setDetailedText(infodetail)
                bayar.exec_()
                try:
                    sql = "INSERT INTO member_event VALUES (%s, %s)"
                    self.mycursor.execute(sql, (self.member_id, self.idEvent))
                    self.mydb.commit()
                except:
                    error = QMessageBox()
                    error.setText("Pendaftara gagal")
                    error.setIcon(QMessageBox.Critical)
                    pass
                message = QMessageBox()
                message.setWindowTitle("Message")
                message.setText("Pendaftaran berhasil")
                message.exec_()

    def back(self):
        self.widget.removeWidget(self)
        # self.widget.setCurrentIndex(self.widget.currentIndex()-1)

###############################################################################################

## MODULES ##

def showDetail(event_id, cur):
    cur.execute(
        """SELECT * FROM event WHERE event_id='%d'"""%(event_id)
    )
    # sukses
    sukses = False
    result = cur.fetchone()
    if(result != None):
        if(result[0] == event_id and result[1]!= None and result[2]!= None and result[3]!= None and result[4]!= None and result[5]!= None):
            sukses = True
    
    return sukses, result

def cekKeterdaftaran(event_id, member_id, cur):
    check = "SELECT * FROM member_event WHERE member_id={} and event_id={}".format(member_id, event_id)
    cur.execute(check)
    result = cur.fetchone()
    if result == None:
        return False
    else:
        return True






# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     DetailEventWindow = QtWidgets.QMainWindow()
#     ui = Ui_DetailEventWindow()
#     ui.setupDatabase()
#     ui.setupUi(DetailEventWindow)
#     DetailEventWindow.show()
#     sys.exit(app.exec_())
