# Interval timer that uses the DS3231 timer chip
# The Alarm (SQW) output from the timer should be connected to the power supply control - active
# low.
#
# Rob Miles March 2020

import smbus
import time

DS3231=0x68

SECONDS_REG=0x00
ALARM1_SECONDS_REG=0x07

CONTROL_REG=0x0E
STATUS_REG=0x0F

class DS3231IntervalTimer():

    def __init__(self, bus):
        self.bus =  bus


    def bcd_to_int(self,bcd):
        return int(('%x' % bcd)[-2:])

    def int_to_bcd(self,x):
        return int(str(x)[-2:], 0x10)


    def write_time_to_clock(self, pos, hours, minutes, seconds):
        self.bus.write_byte_data(DS3231, pos, self.int_to_bcd(seconds))
        self.bus.write_byte_data(DS3231, pos+1, self.int_to_bcd(minutes))
        self.bus.write_byte_data(DS3231, pos+2, self.int_to_bcd(hours))

    def set_alarm1_mask_bits(self,bits):
        pos=ALARM1_SECONDS_REG
        for bit in reversed(bits):
            reg = self.bus.read_byte_data(DS3231, pos) 
            if bit:
                reg = reg|0x80
            else:
                reg = reg&0x7F
            self.bus.write_byte_data(DS3231, pos, reg)
            pos = pos+1
            
    def enable_alarm1(self):
        reg = self.bus.read_byte_data(DS3231, CONTROL_REG)
        self.bus.write_byte_data(DS3231, CONTROL_REG, reg|0x05)
                            
    def clear_alarm1_flag(self):
        reg = self.bus.read_byte_data(DS3231, STATUS_REG)
        self.bus.write_byte_data(DS3231, STATUS_REG, reg&0xFE)
        
    def check_alarm1_triggered(self):
        return self.bus.read_byte_data(DS3231, STATUS_REG)&0x01 != 0

    def set_timer(self, hours, minutes, seconds):
        print("Hours: ", hours, "Minutes: ", minutes, "Seconds: ",seconds)
        # zero the clock
        self.write_time_to_clock(SECONDS_REG, 0, 0, 0)
        # set the alarm
        self.write_time_to_clock(ALARM1_SECONDS_REG, hours, minutes, seconds)
        # set the alarm to match hours minutes and seconds
        # need to set some flags
        self.set_alarm1_mask_bits((True, False, False, False))
        self.enable_alarm1()
        self.clear_alarm1_flag()
    
