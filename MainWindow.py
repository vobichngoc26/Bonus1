# Form implementation generated from reading ui file 'C:\Users\admin\PycharmProjects\K234111E\bonus1\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(685, 236)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 641, 151))
        self.groupBox.setStyleSheet("color: rgb(170, 0, 0);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(170, 170, 127);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 40, 171, 41))
        self.label.setObjectName("label")
        self.lineEditDataset = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditDataset.setGeometry(QtCore.QRect(172, 50, 311, 31))
        self.lineEditDataset.setStyleSheet("color: rgb(170, 0, 0);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(136, 149, 114);")
        self.lineEditDataset.setObjectName("lineEditDataset")
        self.pushButtonOpenFile = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonOpenFile.setGeometry(QtCore.QRect(500, 50, 81, 31))
        self.pushButtonOpenFile.setStyleSheet("color: rgb(170, 0, 0);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(136, 149, 114);")
        self.pushButtonOpenFile.setObjectName("pushButtonOpenFile")
        self.pushButtonSaveChart = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonSaveChart.setGeometry(QtCore.QRect(350, 100, 261, 31))
        self.pushButtonSaveChart.setStyleSheet("color: rgb(170, 0, 0);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(136, 149, 114);")
        self.pushButtonSaveChart.setObjectName("pushButtonSaveChart")
        self.pushButtonOpenChart = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonOpenChart.setGeometry(QtCore.QRect(30, 100, 261, 31))
        self.pushButtonOpenChart.setStyleSheet("color: rgb(170, 0, 0);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(136, 149, 114);")
        self.pushButtonOpenChart.setObjectName("pushButtonOpenChart")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 685, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Võ Bích Ngọc k234111406"))
        self.label.setText(_translate("MainWindow", "Choose Dataset:"))
        self.pushButtonOpenFile.setText(_translate("MainWindow", "..."))
        self.pushButtonSaveChart.setText(_translate("MainWindow", "Save Chart to HTML file"))
        self.pushButtonOpenChart.setText(_translate("MainWindow", "Open Chart in Browser"))
