class PWM_led:
    # a) De init-methode heeft 1 parameter 'pin' waarmee je het pinnummer meegeeft.
    # Dit nummer wordt bijgehouden in een klassevariabele met dezelfde naam.
    # De overeenkomstige pin moet worden ingesteld als output.

    def __init__(self, pin, brightness):
        self.pin = pin
        self.__brightness = brightness
        self.frequency = 1000
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, self.frequency)


    @property
    def brightness(self):
        return self.__brightness

    @brightness.setter
    def brightness(self, value):
        if value < 0 or value > 100:
            raise ValueError("dutycycle must have a value from 0.0 to 100.0")
        else:
            self.__brightness = value
            self.pwm.ChangeDutyCycle(self.brightness)


    def start_pwm(self):
        self.pwm.stop()
        self.pwm.start(self.brightness)

    def __del__(self):
        self.pwm.stop()