#
# Logs data to an MQTT destination
#
#  Rob Miles March 2020

import BME280
import DS3231IntervalTimer
import mqttstore
from machine import I2C
from machine import Pin
import ujson

i2c = I2C(-1, scl=Pin(22), sda=Pin(21))

bme280 = BME280.BME280(i2c=i2c)
ds3231 = DS3231IntervalTimer.DS3231IntervalTimer(i2c)

raw_temp,raw_pressure, raw_humidity = bme280.read_compensated_data()

reading = {}

reading["temp"] = raw_temp/100
reading["pressure"] = (raw_pressure//256)/100
reading["humidity"] = raw_humidity/1024

reading_string = ujson.dumps(reading)

print(reading_string)

mqtt_store = mqttstore.mqttstore("host", "device name", "username", "password", "topic")

if mqtt_store.blocking_connect():
    print("connected - sending data")
    mqtt_store.send_data(reading_string)
    mqtt_store.disconnect()

ds3231.set_timer(hours=0, minutes=0, seconds=30)
