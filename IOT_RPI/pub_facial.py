# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from time import sleep
from gpiozero import MCP3008
from rpi_configure import *

adc = MCP3008(channel=0)


# Custom MQTT message callback
def customCallback(client, userdata, message):
    print("Received a new message: ")
    print(message.payload)
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")


def sendFeatures(features):

    my_rpi = AWSIoTMQTTClient("linux_Machine")
    
    rpi_configure(my_rpi)

    # Connect and subscribe to AWS IoT
    my_rpi.connect()
    my_rpi.subscribe("sensors/camera", 1, customCallback)
    my_rpi.publish("sensors/camera", features, 1)
