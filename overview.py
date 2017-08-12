# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'overview.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from ausgaben import Ui_ausgaben
from db import GruppenkassenDB
from listenansicht import Ui_liste

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets


class Ui_MainWindow(object):
    db = GruppenkassenDB()
    
    def get_number_of_childs(self):
        return len(self.db.get_data_table_childs())
    
    
    def get_rest_money(self):
        money_in = 0
        money_out = 0
        rest_money = 0
        for data in self.db.query_to_dic(self.db.get_data_table_childs()):
            try:
                money_in += int(data['geld'])
            except ValueError:
                pass
        for ausgaben in self.db.query_to_dic(self.db.get_ausgaben()):
            money_out += int(ausgaben['preis'])
        return money_in - money_out
    
    def open_ausgaben(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ausgaben()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def open_push(self):
        self.window_1 = QtWidgets.QMainWindow()
        self.ui = Ui_liste()
        self.ui.setupUi(self.window_1)
        self.window_1.show()
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(565, 600)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 90, 281, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(58, 20, 430, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(90, 160, 125, 19))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.anzahl_children = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.anzahl_children.setFont(font)
        self.anzahl_children.setObjectName("anzahl_children")
        self.horizontalLayout.addWidget(self.anzahl_children)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(240, 160, 185, 19))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.money_total = QtWidgets.QLabel(self.widget1)
        self.money_total.setObjectName("money_total")
        self.horizontalLayout_2.addWidget(self.money_total)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(140, 220, 221, 29))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.money_out = QtWidgets.QPushButton(self.widget2)
        self.money_out.setObjectName("money_out")
        self.money_out.clicked.connect(self.open_ausgaben)
        self.horizontalLayout_3.addWidget(self.money_out)
        self.money_in = QtWidgets.QPushButton(self.widget2)
        self.money_in.setObjectName("money_in")
        self.money_in.clicked.connect(self.open_push)
        self.horizontalLayout_3.addWidget(self.money_in)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 565, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Eine kurze Übersicht"))
        self.label_5.setText(_translate("MainWindow", "Hallo und Herzlich Willkommen"))
        self.label_3.setText(_translate("MainWindow", "Anzahl Kinder:"))
        self.anzahl_children.setText(_translate("MainWindow", str(self.get_number_of_childs())))
        self.label_2.setText(_translate("MainWindow", "Verfügbares Geld in €:"))
        self.money_total.setText(_translate("MainWindow", str(self.get_rest_money())))
        self.money_out.setText(_translate("MainWindow", "Ausgaben"))
        self.money_in.setText(_translate("MainWindow", "Geld einzahlen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

