# Import libraries
import RPi.GPIO as GPIO
import time
import os



def remove():
    try:
        os.remove("led.txt") #remove the led.txt file which contain the sign information
    except:
        print("Exception")
    
  