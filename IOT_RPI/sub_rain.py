# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from time import sleep
from turn_90 import *
from rpi_configure import *



# Custom MQTT message callback
def customCallback(client, userdata, message):
    global temp
    print("Received a new message: ")
    print(message.payload)
    temp = message.payload
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")
    if temp == "open":
        onShields()  #Closes the windows
    else:
        offShields()  #Opens the windows





def subTemp():
    my_rpi = AWSIoTMQTTClient("yeehaww")
    rpi_configure(my_rpi)

    # Connect and subscribe to AWS IoT
    my_rpi.connect()
    my_rpi.subscribe("sensors/motor", 1, customCallback)
    sleep(2)


