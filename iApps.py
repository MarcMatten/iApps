import irsdk
from PyQt5 import QtWidgets, QtCore
import sys
import sysInfo
from GUI.iAppsGUI import Ui_iAppsMainWindow
from UpshiftTone import beep
from UpshiftTone.iRacingUpshiftTone import UpshiftToneClass

ir = irsdk.IRSDK()

class GUIClass(Ui_iAppsMainWindow):
    def __init__(self, window):
        Ui_iAppsMainWindow.__init__(self)
        self.setupUi(window)

        # create and start thread
        self.threadClass = ThreadClass()
        self.threadClass2 = iRThread()
        self.threadClass.start()
        self.threadClass2.start()

        # connect thread signal to GUIClass's sub-function
        self.threadClass.signal.connect(self.updateProgressBar)#
        self.threadClass2.iRRunning.connect(self.updateiR)#

    def updateProgressBar(self, value):
        self.progressBarCPU.setValue(value)

    def updateiR(self, value):
        self.labeliRacingStatus2.setText(value)


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
    iRRunning = QtCore.pyqtSignal(str)

    def __init__(self, parent = None):
        super(iRThread, self).__init__(parent)

    def run(self):
        global startup
        beep.beep()
        while 1:
            self.iRRunning.emit('waiting ...')
            startup = 0
            while ir.startup():
                if not startup == 1:
                    self.iRRunning.emit('connected')
                    startup = 1
                    # put here things to execute when going on track ===================================================
                    # initialisation beep
                    beep.beep(3, 500)

                    # get optimal shift RPM from iRacing and display message
                    ShiftRPM = ir['DriverInfo']['DriverCarSLShiftRPM']

                    # get car and driver information
                    DriverCarIndex = ir['DriverInfo']['DriverCarIdx']
                    DriverCarName = ir['DriverInfo']['Drivers'][DriverCarIndex]['CarScreenNameShort']

                    # display information
                    print('Optimal Shift RPM for', DriverCarName, ':', ShiftRPM)

                    IsOnTrack = False
                else:
                    # put here things to run during on track
                    if ir['IsOnTrack'] and not IsOnTrack:
                        IsOnTrack = True
                        beep.beep(2, 500)
                        self.shiftTone = UpshiftToneClass(ir)

                        self.shiftTone.iRUpshiftTone(ShiftRPM)

                    if not ir['IsOnTrack'] and IsOnTrack:
                        IsOnTrack = False

# start up GUI
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    prog = GUIClass(window)
    window.show()
    app.exec_()