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

    if touch<900:
        cur_led=red
    elif touch>900 and temp<1300:
        cur_led=yellow
    else:
        curl_led=green

    cur_led.value=True
    time.sleep(1)
    cur_led.value=False
    time.sleep(1)

    print("Moisture: " + str(touch))
