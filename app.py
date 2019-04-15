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
from RPi import GPIO
import spidev
from gpiozero import MCP3008

spi = spidev.SpiDev()
btn = 9 #pinnummer aanpassen
rgbled = RGB_led(5, 6, 13)

spi.open(0, 0)  # BUS SPI0, slave on CE 0
spi.max_speed_hz = 10 ** 5  # 100 KHz
potX = MCP3008(0)
potY = MCP3008(1)

btnAmt = 0


#functions --------------------------------------------------------------------------------------------------------------------

def setupGPIO():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(btn, GPIO.FALLING, callback=btn_handler, bouncetime=50)
    GPIO.add_event_callback(btn, btn_handler)

    GPIO.setup(rgbled, GPIO.OUT)

    
    # GPIO.setup([...], GPIO.OUT)
    # GPIO.output([...], GPIO.LOW)


def read_spi(channel):
    spidata = spi.xfer2([1, (8 + channel) << 4, 0])
    return ((spidata[1] & 3) << spidata[2])

def btn_handler():
    btnAmt += 1
    print("er is {} keer op de knop gerdukt".format(btnAmt))
    lcd.lcdStatus()


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

        rgbled.brightnessR()
        rgbled.brightnessG()
        rgbled.brightnessB()

        time.sleep(1)

except KeyboardInterrupt:
    print('Ok bye.')

except Exception as e:
    print(e)

finally:
    GPIO.cleanup()
    spi.close()


#classes --------------------------------------------------------------------------------------------------------------------





class lcd:

    def lcdStatus():
        pass