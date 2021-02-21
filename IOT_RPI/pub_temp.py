# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from time import sleep

import sys
import Adafruit_DHT
from time import sleep
import json
import datetime as datetime
from rpi_configure import *

pin = 17 #CHANGE LATER


	

def submit_temp():
	host = "aq7kwp31awdde-ats.iot.us-east-1.amazonaws.com"     
	rootCAPath = "credential/RootCA.pem"
	certificatePath = "credential/certificate.pem.crt"
	privateKeyPath = "credential/private.pem.key"

	my_rpi = AWSIoTMQTTClient("basicPubSub")
	rpi_configure(my_rpi)

	# Connect to AWS IoT
	my_rpi.connect()
	sleep(2)

	humidity, temperature = Adafruit_DHT.read_retry(11, pin)

	message = {}
	message["deviceid"] = "deviceid_hay"
	now = datetime.datetime.now()
	message["datetimeid"] = now.isoformat()      
	message["temperature"] = temperature
	message["humidity"] = humidity
	my_rpi.publish("sensors/dht", json.dumps(message), 1)
	print(json.dumps(message))
	sleep(7)
