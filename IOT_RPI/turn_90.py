# Import libraries
import RPi.GPIO as GPIO
import time



def onShields():
    # Define variable duty

    angle = 7.0
    servo1.ChangeDutyCycle(angle)
    servo2.ChangeDutyCycle(angle)
    time.sleep(2)
    servo1.start(0)
    servo2.start(0)


def offShields():  
    angle = 2
    servo1.ChangeDutyCycle(angle)
    servo2.ChangeDutyCycle(angle)
    time.sleep(2)
    servo1.start(0)
    servo2.start(0)
 



# Set GPIO numbering mode
GPIO.setmode(GPIO.BCM)

# Set pin 11 as an output, and set servo1 as pin 11 as PWM
GPIO.setup(21,GPIO.OUT)
servo1 = GPIO.PWM(21,50) # Note 11 is pin, 50 = 50Hz pulse
GPIO.setup(5,GPIO.OUT)
servo2 = GPIO.PWM(5,50) # Note 11 is pin, 50 = 50Hz pulse


#start PWM running, but with value of 0 (pulse off)
servo1.start(0)
servo2.start(0)

