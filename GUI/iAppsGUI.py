# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'iAppsGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_iAppsMainWindow(object):
    def setupUi(self, iAppsMainWindow):
        iAppsMainWindow.setObjectName("iAppsMainWindow")
        iAppsMainWindow.setEnabled(True)
        iAppsMainWindow.resize(531, 328)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(iAppsMainWindow.sizePolicy().hasHeightForWidth())
        iAppsMainWindow.setSizePolicy(sizePolicy)
        iAppsMainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        iAppsMainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.widget = QtWidgets.QWidget(iAppsMainWindow)
        self.widget.setMouseTracking(True)
        self.widget.setObjectName("widget")
        self.tabWidget = QtWidgets.QTabWidget(self.widget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 511, 261))
        self.tabWidget.setObjectName("tabWidget")
        self.tabGeneral = QtWidgets.QWidget()
        self.tabGeneral.setObjectName("tabGeneral")
        self.groupBoxiRacing = QtWidgets.QGroupBox(self.tabGeneral)
        self.groupBoxiRacing.setGeometry(QtCore.QRect(9, 9, 241, 121))
        self.groupBoxiRacing.setMouseTracking(False)
        self.groupBoxiRacing.setObjectName("groupBoxiRacing")
        self.progressBarCPU = QtWidgets.QProgressBar(self.groupBoxiRacing)
        self.progressBarCPU.setGeometry(QtCore.QRect(70, 80, 118, 23))
        self.progressBarCPU.setProperty("value", 24)
        self.progressBarCPU.setObjectName("progressBarCPU")
        self.labeliRacingStatus = QtWidgets.QLabel(self.groupBoxiRacing)
        self.labeliRacingStatus.setGeometry(QtCore.QRect(20, 30, 81, 16))
        self.labeliRacingStatus.setObjectName("labeliRacingStatus")
        self.labeliRacingStatus2 = QtWidgets.QLabel(self.groupBoxiRacing)
        self.labeliRacingStatus2.setGeometry(QtCore.QRect(130, 30, 91, 16))
        self.labeliRacingStatus2.setObjectName("labeliRacingStatus2")
        self.tabWidget.addTab(self.tabGeneral, "")
        self.tabUpshiftTone = QtWidgets.QWidget()
        self.tabUpshiftTone.setObjectName("tabUpshiftTone")
        self.groupBox = QtWidgets.QGroupBox(self.tabUpshiftTone)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 221, 231))
        self.groupBox.setObjectName("groupBox")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(20, 20, 161, 17))
        self.checkBox.setObjectName("checkBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tabUpshiftTone)
        self.groupBox_2.setGeometry(QtCore.QRect(240, 0, 251, 231))
        self.groupBox_2.setObjectName("groupBox_2")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox.setGeometry(QtCore.QRect(150, 20, 81, 22))
        self.spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spinBox.setMaximum(20000)
        self.spinBox.setSingleStep(100)
        self.spinBox.setProperty("value", 6000)
        self.spinBox.setObjectName("spinBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 20, 101, 21))
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 50, 101, 21))
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_2.setGeometry(QtCore.QRect(150, 50, 81, 22))
        self.spinBox_2.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spinBox_2.setMaximum(20000)
        self.spinBox_2.setSingleStep(100)
        self.spinBox_2.setProperty("value", 6000)
        self.spinBox_2.setObjectName("spinBox_2")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_4.setGeometry(QtCore.QRect(30, 80, 101, 21))
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setObjectName("checkBox_4")
        self.spinBox_3 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_3.setGeometry(QtCore.QRect(150, 80, 81, 22))
        self.spinBox_3.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spinBox_3.setMaximum(20000)
        self.spinBox_3.setSingleStep(100)
        self.spinBox_3.setProperty("value", 6000)
        self.spinBox_3.setObjectName("spinBox_3")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_5.setGeometry(QtCore.QRect(30, 110, 101, 21))
        self.checkBox_5.setChecked(True)
        self.checkBox_5.setObjectName("checkBox_5")
        self.spinBox_4 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_4.setGeometry(QtCore.QRect(150, 110, 81, 22))
        self.spinBox_4.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spinBox_4.setMaximum(20000)
        self.spinBox_4.setSingleStep(100)
        self.spinBox_4.setProperty("value", 6000)
        self.spinBox_4.setObjectName("spinBox_4")
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_6.setGeometry(QtCore.QRect(30, 140, 101, 21))
        self.checkBox_6.setChecked(True)
        self.checkBox_6.setObjectName("checkBox_6")
        self.spinBox_5 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_5.setGeometry(QtCore.QRect(150, 140, 81, 22))
        self.spinBox_5.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spinBox_5.setMaximum(20000)
        self.spinBox_5.setSingleStep(100)
        self.spinBox_5.setProperty("value", 6000)
        self.spinBox_5.setObjectName("spinBox_5")
        self.checkBox_7 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_7.setGeometry(QtCore.QRect(30, 170, 101, 21))
        self.checkBox_7.setChecked(False)
        self.checkBox_7.setObjectName("checkBox_7")
        self.spinBox_6 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_6.setGeometry(QtCore.QRect(150, 170, 81, 22))
        self.spinBox_6.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spinBox_6.setMaximum(20000)
        self.spinBox_6.setSingleStep(100)
        self.spinBox_6.setProperty("value", 6000)
        self.spinBox_6.setObjectName("spinBox_6")
        self.spinBox_7 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_7.setGeometry(QtCore.QRect(150, 200, 81, 22))
        self.spinBox_7.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spinBox_7.setMaximum(20000)
        self.spinBox_7.setSingleStep(100)
        self.spinBox_7.setProperty("value", 6000)
        self.spinBox_7.setObjectName("spinBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_8.setGeometry(QtCore.QRect(30, 200, 101, 21))
        self.checkBox_8.setChecked(False)
        self.checkBox_8.setObjectName("checkBox_8")
        self.tabWidget.addTab(self.tabUpshiftTone, "")
        iAppsMainWindow.setCentralWidget(self.widget)
        self.menubar = QtWidgets.QMenuBar(iAppsMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 531, 21))
        self.menubar.setObjectName("menubar")
        iAppsMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(iAppsMainWindow)
        self.statusbar.setObjectName("statusbar")
        iAppsMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(iAppsMainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(iAppsMainWindow)

    def retranslateUi(self, iAppsMainWindow):
        _translate = QtCore.QCoreApplication.translate
        iAppsMainWindow.setWindowTitle(_translate("iAppsMainWindow", "iApps"))
        self.groupBoxiRacing.setTitle(_translate("iAppsMainWindow", "iRacing"))
        self.labeliRacingStatus.setText(_translate("iAppsMainWindow", "iRacing Status"))
        self.labeliRacingStatus2.setText(_translate("iAppsMainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGeneral), _translate("iAppsMainWindow", "General"))
        self.groupBox.setTitle(_translate("iAppsMainWindow", "GroupBox"))
        self.checkBox.setText(_translate("iAppsMainWindow", "use iRacing Defaults"))
        self.groupBox_2.setTitle(_translate("iAppsMainWindow", "Set Upshift RPM"))
        self.checkBox_2.setText(_translate("iAppsMainWindow", "1. Gear"))
        self.checkBox_3.setText(_translate("iAppsMainWindow", "2. Gear"))
        self.checkBox_4.setText(_translate("iAppsMainWindow", "3. Gear"))
        self.checkBox_5.setText(_translate("iAppsMainWindow", "4. Gear"))
        self.checkBox_6.setText(_translate("iAppsMainWindow", "5. Gear"))
        self.checkBox_7.setText(_translate("iAppsMainWindow", "6. Gear"))
        self.checkBox_8.setText(_translate("iAppsMainWindow", "7. Gear"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabUpshiftTone), _translate("iAppsMainWindow", "Upshift Tone"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    iAppsMainWindow = QtWidgets.QMainWindow()
    ui = Ui_iAppsMainWindow()
    ui.setupUi(iAppsMainWindow)
    iAppsMainWindow.show()
    sys.exit(app.exec_())

