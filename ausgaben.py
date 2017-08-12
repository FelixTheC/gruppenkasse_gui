# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ausgaben.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ausgaben(object):
    def setupUi(self, ausgaben):
        ausgaben.setObjectName("ausgaben")
        ausgaben.resize(567, 469)
        ausgaben.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(ausgaben)
        self.centralwidget.setObjectName("centralwidget")
        self.ausgaben_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.ausgaben_2.setGeometry(QtCore.QRect(0, 0, 561, 421))
        self.ausgaben_2.setObjectName("ausgaben_2")
        self.uebsicht = QtWidgets.QWidget()
        self.uebsicht.setObjectName("uebsicht")
        self.refresh = QtWidgets.QPushButton(self.uebsicht)
        self.refresh.setGeometry(QtCore.QRect(180, 330, 204, 27))
        self.refresh.setObjectName("refresh")
        self.tableWidget = QtWidgets.QTableWidget(self.uebsicht)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 561, 321))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.ausgaben_2.addTab(self.uebsicht, "")
        self.hinzufuegen = QtWidgets.QWidget()
        self.hinzufuegen.setObjectName("hinzufuegen")
        self.layoutWidget = QtWidgets.QWidget(self.hinzufuegen)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 21, 148, 164))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verwendungszweck = QtWidgets.QLineEdit(self.layoutWidget)
        self.verwendungszweck.setObjectName("verwendungszweck")
        self.verticalLayout_2.addWidget(self.verwendungszweck)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.date = QtWidgets.QDateEdit(self.layoutWidget)
        self.date.setObjectName("date")
        self.verticalLayout_2.addWidget(self.date)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.money = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.money.setObjectName("money")
        self.verticalLayout_2.addWidget(self.money)
        self.layoutWidget1 = QtWidgets.QWidget(self.hinzufuegen)
        self.layoutWidget1.setGeometry(QtCore.QRect(180, 21, 95, 81))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.submit = QtWidgets.QPushButton(self.layoutWidget1)
        self.submit.setObjectName("submit")
        self.verticalLayout.addWidget(self.submit)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.ausgaben_2.addTab(self.hinzufuegen, "")
        ausgaben.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ausgaben)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 567, 25))
        self.menubar.setObjectName("menubar")
        ausgaben.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ausgaben)
        self.statusbar.setObjectName("statusbar")
        ausgaben.setStatusBar(self.statusbar)

        self.retranslateUi(ausgaben)
        self.ausgaben_2.setCurrentIndex(0)
        self.pushButton_2.clicked.connect(self.verwendungszweck.clear)
        self.pushButton_2.clicked.connect(self.money.clear)
        QtCore.QMetaObject.connectSlotsByName(ausgaben)

    def retranslateUi(self, ausgaben):
        _translate = QtCore.QCoreApplication.translate
        ausgaben.setWindowTitle(_translate("ausgaben", "Ausgaben"))
        self.refresh.setText(_translate("ausgaben", "Neuladen"))
        self.ausgaben_2.setTabText(self.ausgaben_2.indexOf(self.uebsicht), _translate("ausgaben", "Uebersicht"))
        self.label.setText(_translate("ausgaben", "Verwendungszweck"))
        self.label_2.setText(_translate("ausgaben", "Datum"))
        self.label_3.setText(_translate("ausgaben", "Preis in Euro"))
        self.submit.setText(_translate("ausgaben", "Eintragen"))
        self.pushButton_2.setText(_translate("ausgaben", "Abbrechen"))
        self.ausgaben_2.setTabText(self.ausgaben_2.indexOf(self.hinzufuegen), _translate("ausgaben", "Ausgabe hinzufuegen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ausgaben = QtWidgets.QMainWindow()
    ui = Ui_ausgaben()
    ui.setupUi(ausgaben)
    ausgaben.show()
    sys.exit(app.exec_())

