import sys
from PyQt5 import QtWidgets, QtCore
from GUI.iAppsGUI import Ui_abc

import sysInfo  # import callback function


class GUIClass(Ui_abc):

    def __init__(self, window):
        Ui_abc.__init__(self)
        self.setupUi(window)
        # creat and start thread
        self.threadClass = ThreadClass()
        self.threadClass.start()
        # connect thread signal to GUIClass's subfunction
        self.threadClass.signal.connect(self.updateProgressBar)

    def updateProgressBar(self, value):
        self.progressBar.setValue(value)


class ThreadClass(QtCore.QThread):

    # create signal object with data type int
    signal = QtCore.pyqtSignal(int)

    def __init__(self, parent = None):
        super(ThreadClass, self).__init__(parent)

    def run(self):
        # run forever
        while 1:
            value = sysInfo.getCPU()    # get data from callback function
            self.signal.emit(value)     # send data via signal

# start up GUI
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    prog = GUIClass(window)
    window.show()
    app.exec_()