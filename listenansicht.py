# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listenansicht.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from db import GruppenkassenDB
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_liste(object):
    db = GruppenkassenDB()
    
    def insert_data_into_db(self):
        if self.dateEdit.text() != '01.01.00':
            erstellt_am=self.dateEdit.text()
        else:
            erstellt_am = "NULL"
        in_db = self.db.get_data_table_childs(self.name_update.text())
        if len(in_db) > 0:
            self.update_db_data()
        else:
            self.db.set_data_into_childs(name=self.name_update.text(), geld=self.money.text(), erstellt_am=erstellt_am)
        
    def update_db_data(self):
        self.db.update_child_data(name=self.name_update.text(), geld=self.money.text())
    
    def load_data_into_table(self):
        self.tableWidget.setRowCount(len(self.db.get_data_table_childs()))
        headers = ['id', 'name', 'bezahlt_bis', 'erstellt_am', 'Geld']
        for n, data in enumerate(self.db.get_data_table_childs()):
            for m, d in enumerate(data):
                newItem = QtWidgets.QTableWidgetItem(str(d))
                self.tableWidget.setItem(n, m, newItem)
        self.tableWidget.setHorizontalHeaderLabels(headers)
        
    def search_specific_name(self):
        self.tableWidget.setRowCount(1)
        headers = ['id', 'name', 'bezahlt_bis', 'erstellt_am', 'Geld']
        for n, data in enumerate(self.db.get_data_table_childs(self.name.text())):
            for m, d in enumerate(data):
                newItem = QtWidgets.QTableWidgetItem(str(d))
                self.tableWidget.setItem(n, m, newItem)
        self.tableWidget.setHorizontalHeaderLabels(headers)        
    
    def setupUi(self, liste):
        liste.setObjectName("liste")
        liste.resize(668, 551)
        self.centralwidget = QtWidgets.QWidget(liste)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 661, 550))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        
        self.refresh = QtWidgets.QPushButton(self.tab)
        self.refresh.setGeometry(QtCore.QRect(470, 330, 180, 27))
        self.refresh.setObjectName("refresh")
        self.refresh.clicked.connect(self.load_data_into_table)
        
        self.search = QtWidgets.QPushButton(self.tab)
        self.search.setGeometry(QtCore.QRect(470, 120, 180, 27))
        self.search.setObjectName("search")
        self.search.clicked.connect(self.search_specific_name)
        
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(470, 150, 180, 27))
        self.pushButton.setObjectName("pushButton")
        
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(470, 10, 180, 91))
        self.label.setObjectName("label")
        self.name = QtWidgets.QLineEdit(self.tab)
        self.name.setGeometry(QtCore.QRect(470, 80, 180, 27))
        self.name.setObjectName("name")
        
        ###################################################
        ########## start Table insert data ################
        ###################################################
        
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 10, 461, 461))
        self.tableWidget.setObjectName("tableWidget")
        self.tabWidget.addTab(self.tab, "")        
        self.tableWidget.setColumnCount(5)
        
        ###################################################
        ############ end Table insert data ################
        ###################################################        
        
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
        name = self.name.text()
        geld = str(self.money.text())
        if self.name.text != "":
            self.submit.clicked.connect(self.insert_data_into_db)
            
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(280, 150, 99, 27))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(310, 80, 67, 17))
        self.label_3.setObjectName("label_3")
        self.dateEdit = QtWidgets.QDateEdit(self.tab_2)
        self.dateEdit.setGeometry(QtCore.QRect(400, 100, 110, 27))
        self.dateEdit.setObjectName("dateEdit")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(400, 80, 151, 17))
        self.label_4.setObjectName("label_4")        
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
        self.tabWidget.setCurrentIndex(0)
        self.pushButton_6.clicked.connect(self.money.clear)
        self.pushButton_6.clicked.connect(self.name_update.clear)
        self.pushButton_6.clicked.connect(self.dateEdit.clear)
        self.pushButton.clicked.connect(self.name.clear)
        QtCore.QMetaObject.connectSlotsByName(liste)
        

    def retranslateUi(self, liste):
        _translate = QtCore.QCoreApplication.translate
        liste.setWindowTitle(_translate("liste", "Liste"))
        self.refresh.setText(_translate("liste", "Neuladen"))
        self.search.setText(_translate("liste", "Suchen"))
        self.pushButton.setText(_translate("liste", "Abbrechen"))
        self.label.setText(_translate("liste", "Bestimmtes Kind anzeigen"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("liste", "Liste"))
        self.label_2.setText(_translate("liste", "Name:"))
        self.submit.setText(_translate("liste", "Eintragen"))
        self.pushButton_6.setText(_translate("liste", "Abbrechen"))
        self.label_3.setText(_translate("liste", "Euro"))
        self.label_4.setText(_translate("liste", "In der Gruppe seit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("liste", "Neuer Eintrag"))

    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    liste = QtWidgets.QMainWindow()
    ui = Ui_liste()
    ui.setupUi(liste)
    liste.show()
    ui.load_data_into_table()
    sys.exit(app.exec_())

