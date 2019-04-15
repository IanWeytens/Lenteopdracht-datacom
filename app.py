# txd -> arduino
# rxd -> arduino
# ceo -> mpc3008
# sda -> lcd
# scl -> lcd
#  -> joystickbtn
# mosi -> mpc3008
# miso -> mpc3008
# sclk -> mpc3008
# gpio 5 -> rgb r
# gpio 6 -> rgb g
# gpio 13 -> rgb b

import time
import spidev

from subprocess import check_output
from datetime import time, date, datetime, timedelta
from RPi import GPIO
from gpiozero import MCP3008
from smbus import SMBus

from modules.pwm import PWM_led
from modules.rgb import RGB_led
#from modules.lcd import LCD


spi = spidev.SpiDev()
btn = 9 #pinnummer aanpassen
rgbled = RGB_led(5, 6, 13)

spi.open(0, 0)  # BUS SPI0, slave on CE 0
spi.max_speed_hz = 10 ** 5  # 100 KHz

potX = MCP3008(0)
potY = MCP3008(1)
i2c = SMBus(1)

btnAmt = 0
lcdStat = 1


#functions --------------------------------------------------------------------------------------------------------------------

def setupGPIO():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(btn, GPIO.FALLING, callback=btn_handler, bouncetime=50)
    GPIO.add_event_callback(btn, btn_handler)

    GPIO.setup(rgbled, GPIO.OUT)

    # GPIO.setup([...], GPIO.OUT)
    # GPIO.output([...], GPIO.LOW)

def int2bcd(value):
    """
    Convert 2-digit value to BCD encoded byte
    :param value: number to convert (int)
    :return: BCD encoded number (int)
    """
    if value < 10:
        getal1 = int(str(value))
        getal2 = 0
    else:
        getal1 = int(str(value)[1])
        getal2 = int(str(value)[0]) << 4

    bcd = getal1 + getal2
    #print(bcd)
    return bcd

def lcdStatus():
        global lcdStat
        if(lcdStat == 1): 
            #ip adressen
            ips = check_output(['hostname', '--all-ip-addresses'])
            print(ips)
            ip = ips.split()
            print(ip[0])
            print(ip[1])
            print(ip[2])


        elif(lcdStat == 2):
            
            #VRX waarde



        elif(lcdStat == 3):
            #VRY waarde

            


def set_seconds_register(value):
    """
    Set the contents of the DS1307 SECONDS register
    :param value: new register value (int)
    :return: None
    """
    i2c.write_byte_data(int2bcd(value))

def read_spi(channel):
    spidata = spi.xfer2([1, (8 + channel) << 4, 0])
    return ((spidata[1] & 3) << spidata[2])

def btn_handler():
    global btnAmt
    btnAmt += 1
    print("er is {} keer op de knop gerdukt".format(btnAmt))
    lcdStatus()


#loop --------------------------------------------------------------------------------------------------------------------

try:
    setupGPIO()

    while True:
        
        channelpotX = read_spi(0)
        percentageX = round(potX.value *100)
        print("PotX: Waarde = {}, Percentage = {}".format(channelpotX, percentageX))

        channelpotY = read_spi(1)
        percentageY = round(potY.value *100)
        print("PotY: Waarde = {}, Percentage = {}%".format(channelpotY, percentageY))

        rgbled.brightnessR(percentageY) #wrong values, need 0-255
        rgbled.brightnessG(percentageY)
        rgbled.brightnessB(percentageY)

        lcdStatus()

        time.sleep(1)

except KeyboardInterrupt:
    print('Ok bye.')

except Exception as e:
    print(e)

finally:
    GPIO.cleanup()
    spi.close()
