from classes.pwm import PWM_led

class RGB_led:
    # a) de init-methode krijgt 3 parameters; 'red', 'green', 'blue' mee die verwijzen naar de resp. pinnummers waarop
    # de RGB-LED is aangesloten. Je maakt 3 overeenkomstige klassevariabelen waarin je telkens een LED-object
    # initialiseert op de overeenkomstige pin, en met brightness 0

    def __init__(self, pinR, pinG, pinB):
        self.__brightnessR = 50
        self.__brightnessG = 50
        self.__brightnessB = 50

        self.pinR = PWM_led(pinR, self.__brightnessR)
        self.pinG = PWM_led(pinG, self.__brightnessG)
        self.pinB = PWM_led(pinB, self.__brightnessB)


    @property
    def brightnessR(self):
        return self.__brightnessR

    @brightnessR.setter
    def brightnessR(self, value):
        if value < 0 or value > 255:
            raise ValueError("De waarde moet tussen 0 en 255 liggen.")
        else:
            self.__brightnessR = float(value) / 255 * 100
            self.pinR.pwm.ChangeDutyCycle(self.__brightnessR)

    @property
    def brightnessG(self):
        return self.__brightnessG
    @brightnessG.setter
    def brightnessG(self, value):
        if value < 0 or value > 255:
            raise ValueError("De waarde moet tussen 0 en 255 liggen.")
        else:
            self.__brightnessG = float(value) / 255 * 100
            self.pinG.pwm.ChangeDutyCycle(self.__brightnessG)

    @property
    def brightnessB(self):
        return self.__brightnessB
    @brightnessB.setter
    def brightnessB(self, value):
        if value < 0 or value > 255:
            raise ValueError("De waarde moet tussen 0 en 255 liggen.")
        else:
            self.__brightnessB = float(value) / 255 * 100
            self.pinB.pwm.ChangeDutyCycle(self.__brightnessB)


    def start_pwm(self):
        self.pinR.pwm.stop()
        self.pinG.pwm.stop()
        self.pinB.pwm.stop()
        self.pinR.start_pwm()
        self.pinG.start_pwm()
        self.pinB.start_pwm()