# Import libraries
import RPi.GPIO as GPIO
import time
from pub_temp import *
from button_face_recognition import *
from pub_rain_detected import *
from pub_sub_sign import *
from sub_rain import *



def subAll():

    changeSign()  #From pub_suub_sign.py, purpose is to subscribe to the topic to get the string

    checkButton() #From button_face_recognition.py, it will if the button is pressed and will conduct conditions within the file if buttons are pressed for face recognition

    subTemp() #From the sub_rain.py, will subscribe to the topic to recieve information to on or off the window