# Interval timer that uses the DS3231 timer chip
# The Alarm (SQW) output from the timer should be connected to the power supply control - active
# low.
#
# Rob Miles March 2020

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
        
        buffer=bytearray(3)
        
        buffer[0]=self.int_to_bcd(seconds)
        buffer[1]=self.int_to_bcd(minutes)
        buffer[2]=self.int_to_bcd(hours)
        
        self.bus.writeto_mem(DS3231, pos, buffer)

    def set_alarm1_mask_bits(self,bits):
        
        buffer=bytearray(1)
        
        pos=ALARM1_SECONDS_REG
        
        for bit in reversed(bits):
            self.bus.readfrom_mem_into(DS3231, pos, buffer) 
            if bit:
                buffer[0] = buffer[0]|0x80
            else:
                buffer[0] = buffer[0]&0x7F
            self.bus.writeto_mem(DS3231, pos, buffer)
            pos = pos+1
            
    def enable_alarm1(self):
        buffer=bytearray(1)
        self.bus.readfrom_mem_into(DS3231, CONTROL_REG, buffer)
        buffer[0] = buffer[0]|0x05
        self.bus.writeto_mem(DS3231, CONTROL_REG, buffer)
                            
    def clear_alarm1_flag(self):
        buffer=bytearray(1)
        self.bus.readfrom_mem_into(DS3231, STATUS_REG, buffer)
        buffer[0] = buffer[0]&0xFE
        self.bus.writeto_mem(DS3231, STATUS_REG, buffer)


    def check_alarm1_triggered(self):
        buffer=bytearray(1)
        self.bus.readfrom_mem_into(DS3231, STATUS_REG, buffer)
        return buffer[0]&0x01 != 0

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
    
