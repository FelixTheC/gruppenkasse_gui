# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listenansicht.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_liste(object):
    def setupUi(self, liste):
        liste.setObjectName("liste")
        liste.resize(568, 451)
        self.centralwidget = QtWidgets.QWidget(liste)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 561, 401))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.overview = QtWidgets.QPushButton(self.tab)
        self.overview.setGeometry(QtCore.QRect(380, 330, 171, 27))
        self.overview.setObjectName("overview")
        self.ausgaben = QtWidgets.QPushButton(self.tab)
        self.ausgaben.setGeometry(QtCore.QRect(380, 300, 171, 27))
        self.ausgaben.setObjectName("ausgaben")
        self.search = QtWidgets.QPushButton(self.tab)
        self.search.setGeometry(QtCore.QRect(370, 140, 180, 27))
        self.search.setObjectName("search")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(370, 173, 180, 27))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(370, 10, 180, 91))
        self.label.setObjectName("label")
        self.name = QtWidgets.QLineEdit(self.tab)
        self.name.setGeometry(QtCore.QRect(370, 107, 180, 27))
        self.name.setObjectName("name")
        self.listView = QtWidgets.QListView(self.tab)
        self.listView.setGeometry(QtCore.QRect(0, 0, 371, 361))
        self.listView.setObjectName("listView")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.name_update = QtWidgets.QLineEdit(self.tab_2)
        self.name_update.setGeometry(QtCore.QRect(160, 100, 141, 27))
        self.name_update.setObjectName("name_update")
        self.money = QtWidgets.QSpinBox(self.tab_2)
        self.money.setGeometry(QtCore.QRect(310, 100, 71, 27))
        self.money.setObjectName("money")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(160, 80, 67, 17))
        self.label_2.setObjectName("label_2")
        self.submit = QtWidgets.QPushButton(self.tab_2)
        self.submit.setGeometry(QtCore.QRect(160, 150, 99, 27))
        self.submit.setObjectName("submit")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(280, 150, 99, 27))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(310, 80, 67, 17))
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab_2, "")
        liste.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(liste)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 568, 25))
        self.menubar.setObjectName("menubar")
        liste.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(liste)
        self.statusbar.setObjectName("statusbar")
        liste.setStatusBar(self.statusbar)

        self.retranslateUi(liste)
        self.tabWidget.setCurrentIndex(1)
        self.pushButton_6.clicked.connect(self.money.clear)
        self.pushButton_6.clicked.connect(self.name_update.clear)
        self.pushButton.clicked.connect(self.name.clear)
        QtCore.QMetaObject.connectSlotsByName(liste)

    def retranslateUi(self, liste):
        _translate = QtCore.QCoreApplication.translate
        liste.setWindowTitle(_translate("liste", "Liste"))
        self.overview.setText(_translate("liste", "Übersicht"))
        self.ausgaben.setText(_translate("liste", "Ausgaben"))
        self.search.setText(_translate("liste", "Suchen"))
        self.pushButton.setText(_translate("liste", "Abbrechen"))
        self.label.setText(_translate("liste", "Bestimmtes Kind anzeigen"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("liste", "Liste"))
        self.label_2.setText(_translate("liste", "Name:"))
        self.submit.setText(_translate("liste", "Eintragen"))
        self.pushButton_6.setText(_translate("liste", "Abbrechen"))
        self.label_3.setText(_translate("liste", "Euro"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("liste", "Neuer Eintrag"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    liste = QtWidgets.QMainWindow()
    ui = Ui_liste()
    ui.setupUi(liste)
    liste.show()
    sys.exit(app.exec_())

