# RTC-controlled-data-logger ESP32 Version

This version of the logging program runs in MicroPython on an ESP32/ESP8266. As supplied it logs temperature, air pressure and humidity to an MQTT broker. To get it going do the following:

1.  Build the circuit with a DS3231 and a BME280 connected to the I2C. The configuration is for an ESP32 DOIT board which has I2C connected to pins 22 (SCL) and 21 (SDA). You can modify these values in main.py to reflect your hardware. The alarm output from the DS3231 should be connected to the power control so that when alarm is sounding the power is switched on.
2.  Install MicroPython from here:

~~~
https://micropython.org/download/#esp32 
~~~

2. Use a tool such as Thonny (https://thonny.org/) to copy the Python files onto your device. 
3. Edit the file boot.py and insert your WiFi SSID and password. 
4. Reboot your device and make sure that it can connect to the network. Now you need to install some libraries. Type the following commands into the REPL command prompt:
~~~
import upip
upip.install('micropython-bme280')
upip.install('micropython-umqtt.robust')
upip.install('micropython-umqtt.simple')
~~~

5. Edit the main.py file and set the credentials for your MQTT broker and the publish topic.
6. M


Have fun

Rob Miles March 2020
