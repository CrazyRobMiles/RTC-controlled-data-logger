#
# Logs data to an MQTT destination
#
#  Rob Miles March 2020

import smbus
import BME280
import DS3231IntervalTimer
import mqttstore
import json

bus=smbus.SMBus(1)

bme280 = BME280.BME280(bus)
ds3231 = DS3231IntervalTimer.DS3231IntervalTimer(bus)

temperature,pressure,humidity = bme280.readBME280All()

reading = {}

reading["temp"] = temperature
reading["pressure"] = pressure
reading["humidity"] = humidity

reading_string = json.dumps(reading)

print(reading_string)

mqtt_store = mqttstore.mqttstore("host url", "sensor name", "username", "password","topic")

if mqtt_store.blocking_connect():
    print("connected - sending data")
    mqtt_store.send_data(reading_string)
    mqtt_store.disconnect()


ds3231.set_timer(hours=0, minutes=0, seconds=30)


