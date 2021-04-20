# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hasilSearch.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi


class Ui_searchWindow(QMainWindow):
    widget = []
    arrofEvent = []
    numofEvent = 0

    def __init__(self, widget, arrofEvent, parent=None):
        super().__init__()
        self.widget = widget
        self.widget.addWidget(self)
        self.arrofEvent = arrofEvent
        self.numofEvent = len(arrofEvent)
        # self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
        loadUi("hasilSearch.ui", self)
        self.setupUi(self)
        print("Num of Event: " , self.numofEvent)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(890, 732)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.addButton(self.arrofEvent)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 70, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 890, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.back)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Back"))
        self.label.setText(_translate("MainWindow", "Hasil Search"))

    def addButton(self, arrofEvent) : 
        for i in range(len(arrofEvent)) : 
            if (i == 0) :
                self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton1.setGeometry(QtCore.QRect(50, 160, 161, 181))
            elif (i == 1) : 
                self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton2.setGeometry(QtCore.QRect(260, 160, 161, 181))
            elif (i == 2) : 
                self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton3.setGeometry(QtCore.QRect(470, 160, 161, 181))
            elif (i == 3) : 
                self.pushButton4 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton4.setGeometry(QtCore.QRect(680, 160, 161, 181))
            elif (i == 4) :
                self.pushButton5 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton5.setGeometry(QtCore.QRect(50, 420, 161, 181))
            elif (i == 5) : 
                self.pushButton6 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton6.setGeometry(QtCore.QRect(260, 420, 161, 181))
            elif (i == 6) :
                self.pushButton7 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton7.setGeometry(QtCore.QRect(470, 420, 161, 181))
            elif (i == 7) : 
                self.pushButton8 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton8.setGeometry(QtCore.QRect(680, 160, 161, 181))

    def back(self):
        self.widget.removeWidget(self)
        self.widget.setCurrentIndex(self.widget.currentIndex()-1)

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
