import sys
from PyQt5 import QtWidgets, QtCore
from GUI.iAppsGUI import Ui_iAppsMainWindow
from UpshiftTone.iRacingUpshiftTone import irUpshiftSound

import sysInfo  # import callback function
#from guiLoop import guiLoop # https://gist.github.com/niccokunzmann/8673951


class GUIClass(Ui_iAppsMainWindow):
    def __init__(self, window):
        Ui_iAppsMainWindow.__init__(self)
        self.setupUi(window)
        # creat and start thread
        self.threadClass = ThreadClass()
        self.threadClass2 = iRThread()
        self.threadClass.start()
        self.threadClass2.start()
        # connect thread signal to GUIClass's subfunction
        self.threadClass.signal.connect(self.updateProgressBar)#
    def updateProgressBar(self, value):
        self.progressBarCPU.setValue(value)
        self.labeliRacingStatus2.setNum(value)


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

class iRThread(QtCore.QThread):

    def __init__(self, parent = None):
        super(iRThread, self).__init__(parent)

    def run(self):
        irUpshiftSound()


# start up GUI
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    prog = GUIClass(window)
    window.show()
    app.exec_()