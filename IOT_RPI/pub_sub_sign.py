# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from time import sleep

import sys
import Adafruit_DHT
from rpi_lcd import LCD
import sys
import json
import datetime as datetime
import os
from rpi_configure import *

# Custom MQTT message callback
def customCallback(client, userdata, message): #get the updated string for the sign from the topic
	print("Received a new message: ")
	print(message.payload)
	message = message.payload
	lcd = LCD()
	data = message.split(":") #split the message from user, string contains a : to seperate row 1 and row 2 for LCD
	lcd.text(data[0],1) #display text onto row 1 of lcd
	lcd.text(data[1],2) #display text onto row 2 of lcd
	print("--------------\n\n")
	f = open("led.txt","w")
	f.write(message)
	f.close()

def changeSign(): #subscribing to the topic to get the string
	my_rpi = AWSIoTMQTTClient("signSub")
	rpi_configure(my_rpi)

	# Connect and subscribe to AWS IoT
	my_rpi.connect()
	my_rpi.subscribe("output/sign", 1, customCallback)

def sign():
	my_rpi = AWSIoTMQTTClient("signSub")
	changeSign()
	if os.path.isfile('led.txt'): #checking if the file is created (if created means user input new text for sign)
		print("publishing")
		f = open("led.txt", "r")
		data = f.read()
		print(data)
		my_rpi.publish("input/sign", data, 1) #publishing the message on LCD for the webserver
	print("waiting")
	sleep(5)
