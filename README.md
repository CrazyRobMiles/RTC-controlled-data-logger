# RTC-controlled-data-logger

Uses the DS3231 alarm output to control a data logger

This example program reads environmental information from a BME280 sensor and then posts it to an MQTT broker. 

The timer uses an alarm in a DS3231 device to control the reading interval. The alarm  output from the DS3231 can be used to control the power to the device, so that it can be shut down in between readings. 

There are two versions of the application, one for Python 3 on the Raspberry Pi and the other for MicroPython running on an ESP32 or ESP8266.

Have fun

Rob Miles April 2020
