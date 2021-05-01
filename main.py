import board
import digitalio
import time
import busio
import smtplib
import ssl
from board import SCL, SDA
from adafruit_seesaw.seesaw import Seesaw

i2c_bus = busio.I2C(SCL, SDA)

ss = Seesaw(i2c_bus, addr=0x36)

green=digitalio.DigitalInOut(board.D18)
red=digitalio.DigitalInOut(board.D23)
yellow=digitalio.DigitalInOut(board.D24)

green.direction=digitalio.Direction.OUTPUT
red.direction=digitalio.Direction.OUTPUT
yellow.direction=digitalio.Direction.OUTPUT

while True:
    # read moisture level through capacitive touch pad
    touch = ss.moisture_read()

    # read temperature from the temperature sensor
    temp = ss.get_temp()

    if touch<900:
        cur_led=red
        #red.value=True
        #time.sleep(1)
        #red.value=False
        #time.sleep(1)
    elif touch>900 and temp<1300:
        cur_led=yellow
        #yellow.value=True
        #time.sleep(1)
        #yellow.value=False
        #time.sleep(1)
    else:
        curl_led=green
        #green.value=True
        #time.sleep(1)
        #green.value=False
        #time.sleep(1)

    cur_led.value=True
    time.sleep(1)
    cur_led.value=False
    time.sleep(1)

    print("temp: " + str(temp) + "  moisture: " + str(touch))