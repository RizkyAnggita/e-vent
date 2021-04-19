# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test1.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from showDetailEvent import Ui_DetailEventWindow

mydb = mysql.connector.connect(
    host = "localhost",
    user = "admin",
    passwd = "admin",
    database = "e_vent"
)

class Ui_EventWindow(QMainWindow):
    widget = []

    def __init__(self, widget, parent=None):
        super().__init__()
        self.widget = widget
        self.widget.addWidget(self)
        # self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
        loadUi("pageEvent.ui", self)
        self.setupUi(self)
        # self.HotEvent1.clicked.connect(self.test)
        # # self.centralwidget.clicked.connect(self.test)
        # print(self.HotEvent1.metaObject().className())
        # # for event in self.Q:
        # #     if event.metaObject().className() == "QPushButton":
        # #         print("HEHE")
        # print(self.QtWidgets.QPushButton.count())
        
    def test(self):
        print("KEPENCET")
    
    def setupUi(self, EventWindow):
        EventWindow.setObjectName("EventWindow")
        EventWindow.resize(890, 732)
        self.centralwidget = QtWidgets.QWidget(EventWindow)
        self.centralwidget.setObjectName("centralwidget")
        # self.centralwidget.setStyleSheet("background-color : #ffffff")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 891, 61))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(350, 20, 93, 28))
        self.pushButton.setText("Search")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setIcon(QtGui.QIcon("images/loupe.png"))
        self.SearchBar = QtWidgets.QLineEdit(self.frame)
        self.SearchBar.setGeometry(QtCore.QRect(110, 20, 231, 28))
        self.SearchBar.setObjectName("SearchBar")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 130, 851, 191))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.HotEvent1 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HotEvent1.sizePolicy().hasHeightForWidth())
        self.HotEvent1.setSizePolicy(sizePolicy)
        self.HotEvent1.setText("")
        self.HotEvent1.setObjectName("HotEvent1")
        self.HotEvent1.setStyleSheet("border-image:url(images/event.png)")
        self.horizontalLayout.addWidget(self.HotEvent1)
        self.HotEvent2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HotEvent2.sizePolicy().hasHeightForWidth())
        self.HotEvent2.setSizePolicy(sizePolicy)
        self.HotEvent2.setText("")
        self.HotEvent2.setObjectName("HotEvent2")
        self.horizontalLayout.addWidget(self.HotEvent2)
        self.HotEvent3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HotEvent3.sizePolicy().hasHeightForWidth())
        self.HotEvent3.setSizePolicy(sizePolicy)
        self.HotEvent3.setText("")
        self.HotEvent3.setObjectName("HotEvent3")
        self.horizontalLayout.addWidget(self.HotEvent3)
        self.HotEvent4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.HotEvent4.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HotEvent4.sizePolicy().hasHeightForWidth())
        self.HotEvent4.setSizePolicy(sizePolicy)
        self.HotEvent4.setText("")
        self.HotEvent4.setObjectName("HotEvent4")
        self.horizontalLayout.addWidget(self.HotEvent4)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 330, 851, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.HotEventName1 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.HotEventName1.setAlignment(QtCore.Qt.AlignCenter)
        self.HotEventName1.setObjectName("HotEventName1")
        self.horizontalLayout_2.addWidget(self.HotEventName1)
        self.HotEventName2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.HotEventName2.setAlignment(QtCore.Qt.AlignCenter)
        self.HotEventName2.setObjectName("HotEventName2")
        self.horizontalLayout_2.addWidget(self.HotEventName2)
        self.HotEventName3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.HotEventName3.setAlignment(QtCore.Qt.AlignCenter)
        self.HotEventName3.setObjectName("HotEventName3")
        self.horizontalLayout_2.addWidget(self.HotEventName3)
        self.HotEventName4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.HotEventName4.setAlignment(QtCore.Qt.AlignCenter)
        self.HotEventName4.setObjectName("HotEventName4")
        self.horizontalLayout_2.addWidget(self.HotEventName4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 80, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 430, 851, 191))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.NewEvent1 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NewEvent1.sizePolicy().hasHeightForWidth())
        self.NewEvent1.setSizePolicy(sizePolicy)
        self.NewEvent1.setText("")
        self.NewEvent1.setObjectName("NewEvent1")
        self.horizontalLayout_3.addWidget(self.NewEvent1)
        self.NewEvent2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NewEvent2.sizePolicy().hasHeightForWidth())
        self.NewEvent2.setSizePolicy(sizePolicy)
        self.NewEvent2.setText("")
        self.NewEvent2.setObjectName("NewEvent2")
        self.horizontalLayout_3.addWidget(self.NewEvent2)
        self.NewEvent3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NewEvent3.sizePolicy().hasHeightForWidth())
        self.NewEvent3.setSizePolicy(sizePolicy)
        self.NewEvent3.setText("")
        self.NewEvent3.setObjectName("NewEvent3")
        self.horizontalLayout_3.addWidget(self.NewEvent3)
        self.NewEvent4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.NewEvent4.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NewEvent4.sizePolicy().hasHeightForWidth())
        self.NewEvent4.setSizePolicy(sizePolicy)
        self.NewEvent4.setText("")
        self.NewEvent4.setObjectName("NewEvent4")
        self.horizontalLayout_3.addWidget(self.NewEvent4)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 380, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(20, 630, 851, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.NewEventName1 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.NewEventName1.setAlignment(QtCore.Qt.AlignCenter)
        self.NewEventName1.setObjectName("NewEventName1")
        self.horizontalLayout_4.addWidget(self.NewEventName1)
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        EventWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EventWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 890, 26))
        self.menubar.setObjectName("menubar")
        EventWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EventWindow)
        self.statusbar.setObjectName("statusbar")
        EventWindow.setStatusBar(self.statusbar)

        self.retranslateUi(EventWindow)
        self.retranslateNewEvent(EventWindow)
        self.retranslateNearestEvent(EventWindow)
        self.pushButton.clicked.connect(self.search)
        QtCore.QMetaObject.connectSlotsByName(EventWindow)

    def retranslateUi(self, EventWindow):
        _translate = QtCore.QCoreApplication.translate
        EventWindow.setWindowTitle(_translate("EventWindow", "MainWindow"))
        self.label_6.setText(_translate("EventWindow", "E-Vent"))
        self.label_5.setText(_translate("EventWindow", "Hot Event"))
        self.label_7.setText(_translate("EventWindow", "New Event"))

    def retranslateNewEvent(self,EventWindow) :
        mycursor = mydb.cursor()
        sql = 'SELECT namaEvent, event_id FROM event ORDER BY event_id DESC;'
        mycursor.execute(sql)
        result = mycursor.fetchall()
        _translate = QtCore.QCoreApplication.translate
        self.NewEventName1.setText(_translate("EventWindow", result[0][0]))
        self.label_9.setText(_translate("EventWindow", result[1][0]))
        self.label_10.setText(_translate("EventWindow", result[2][0]))
        self.label_11.setText(_translate("EventWindow", result[3][0]))
        
        self.NewEvent1.clicked.connect(lambda: self.gotoDetail(result[0][1]))
        self.NewEvent2.clicked.connect(lambda: self.gotoDetail(result[1][1]))
        self.NewEvent3.clicked.connect(lambda: self.gotoDetail(result[2][1]))
        self.NewEvent4.clicked.connect(lambda: self.gotoDetail(result[3][1]))

        

    def retranslateNearestEvent(self, EventWindow) :
        mycursor = mydb.cursor()
        sql = "SELECT namaEvent, event_id FROM event ORDER BY ABS(DATEDIFF(tanggal, NOW()));"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        _translate = QtCore.QCoreApplication.translate
        self.HotEventName1.setText(_translate("EventWindow", result[0][0]))
        self.HotEventName2.setText(_translate("EventWindow", result[1][0]))
        self.HotEventName3.setText(_translate("EventWindow", result[2][0]))
        self.HotEventName4.setText(_translate("EventWindow", result[3][0]))
        
        self.HotEvent1.clicked.connect(lambda: self.gotoDetail(result[0][1]))
        self.HotEvent2.clicked.connect(lambda: self.gotoDetail(result[1][1]))
        self.HotEvent3.clicked.connect(lambda: self.gotoDetail(result[2][1]))
        self.HotEvent4.clicked.connect(lambda: self.gotoDetail(result[3][1]))

    
    def gotoDetail(self, id):
        showDetailEvent = Ui_DetailEventWindow(self.widget, id)
        self.widget.addWidget(showDetailEvent)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def search(self) :
        name = self.SearchBar.text()
        mycursor = mydb.cursor()
        sql = "SELECT namaEvent FROM event"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for x in result :
            low = x[0].lower()
            arr = low.split()
            if (name.lower() in arr) : 
                print(x[0])



# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     EventWindow = QtWidgets.QMainWindow()
#     ui = Ui_EventWindow()
#     ui.setupUi(EventWindow)
#     EventWindow.show()
#     sys.exit(app.exec_())
