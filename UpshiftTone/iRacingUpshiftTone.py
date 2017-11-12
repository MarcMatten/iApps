from pygame import *
from UpshiftTone import beep

class UpshiftToneClass(object):
    def __init__(self, ir):
        self.ir = ir
        #self.fname = fname
        print(self.ir)

    def iRUpshiftTone(self, ShiftRPM):

        print('function called')

        while self.ir['IsOnTrack']:
            RPM = self.ir['RPM']
            Gear = self.ir['Gear']

            #	check if upshift RPM is reached
            if Gear > 0 and RPM >= ShiftRPM:  # disable sound for neutral and reverse gear
                beep.beep(1, 1000)
                time.wait(1000)