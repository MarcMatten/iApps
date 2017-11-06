# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'iAppsGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_abc(object):
    def setupUi(self, abc):
        abc.setObjectName("abc")
        abc.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(abc)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(250, 70, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        abc.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(abc)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        abc.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(abc)
        self.statusbar.setObjectName("statusbar")
        abc.setStatusBar(self.statusbar)

        self.retranslateUi(abc)
        QtCore.QMetaObject.connectSlotsByName(abc)

    def retranslateUi(self, abc):
        _translate = QtCore.QCoreApplication.translate
        abc.setWindowTitle(_translate("abc", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    abc = QtWidgets.QMainWindow()
    ui = Ui_abc()
    ui.setupUi(abc)
    abc.show()
    sys.exit(app.exec_())

