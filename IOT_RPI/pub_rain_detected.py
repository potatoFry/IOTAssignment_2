# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from time import sleep
from gpiozero import Buzzer, InputDevice, DigitalInputDevice
import RPi.GPIO as GPIO
from random import randint
from turn_90 import *
from rpi_configure import *


def rain_detected():

    my_rpi = AWSIoTMQTTClient("skrt")
    rpi_configure(my_rpi)

    # Connect to AWS IoT
    my_rpi.connect()
    my_rpi.publish("detectors/rain", "Rain detected, windows are now closed", 1)
    onShields() #This function is from turn_90.py which closes the windows 


def getRain():
    GPIO.setmode(GPIO.BCM)  #setting up of the GPIO
    GPIO.setup(22,GPIO.IN)
    rain = GPIO.input(22)   #topic is detectors/rain
    return rain