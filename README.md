# RTC-controlled-data-logger

Uses the DS3231 alarm output to control a data logger

This example program reads environmental information from a BME280 sensor and then posts it to an MQTT broker. 

The timer uses an alarm in a DS3231 device to control the reading interval. The alarm  output from the DS3231 can be used to control the power to the device, so that it can be shut down in between readings. 

Have fun

Rob Miles March 2020
