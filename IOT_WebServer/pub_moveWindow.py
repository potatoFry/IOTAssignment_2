# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from time import sleep
from random import randint

# Custom MQTT message callback
def customCallback(client, userdata, message):
    print("Received a new message: ")
    print(message.payload)
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")


def windowOpen():
    host = "aq7kwp31awdde-ats.iot.us-east-1.amazonaws.com"
    rootCAPath = "credential/RootCA.pem"
    certificatePath = "credential/certificate.pem.crt"
    privateKeyPath = "credential/private.pem.key"

    my_rpi = AWSIoTMQTTClient("linux_Machine")
    my_rpi.configureEndpoint(host, 8883)
    my_rpi.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

    my_rpi.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
    my_rpi.configureDrainingFrequency(2)  # Draining: 2 Hz
    my_rpi.configureConnectDisconnectTimeout(10)  # 10 sec
    my_rpi.configureMQTTOperationTimeout(5)  # 5 sec

    # Connect and subscribe to AWS IoT
    my_rpi.connect()
    my_rpi.subscribe("sensors/motor", 1, customCallback)
    my_rpi.publish("sensors/motor", "open", 1)


def windowClose():
    host = "aq7kwp31awdde-ats.iot.us-east-1.amazonaws.com"
    rootCAPath = "credential/RootCA.pem"
    certificatePath = "credential/certificate.pem.crt"
    privateKeyPath = "credential/private.pem.key"

    my_rpi = AWSIoTMQTTClient("linux_Machine")
    my_rpi.configureEndpoint(host, 8883)
    my_rpi.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

    my_rpi.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
    my_rpi.configureDrainingFrequency(2)  # Draining: 2 Hz
    my_rpi.configureConnectDisconnectTimeout(10)  # 10 sec
    my_rpi.configureMQTTOperationTimeout(5)  # 5 sec

    # Connect and subscribe to AWS IoT
    my_rpi.connect()
    my_rpi.subscribe("sensors/motor", 1, customCallback)
    my_rpi.publish("sensors/motor", "close", 1)
