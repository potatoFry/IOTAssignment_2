import boto3
import botocore
from gpiozero import Button
from signal import pause
from time import sleep
import datetime
import json
import pub_facial

button = Button(13, pull_up=False) #making the button
BUCKET = 'hay-iot' # replace with your own unique bucket name
location = {'LocationConstraint': 'us-east-1'} #values for the location of bucket

def takePhoto():
    today = datetime.datetime.now() #getting date and time for a unique file name
    today = today.strftime("%Y-%m-%d-%H:%M:%S")
    file_path = "/home/pi/IOT_Assignment2/visitor/" #file path of where to store the photo of visitor
    file_name = str(today) + "-visitor.jpg" #file name of the actual photo of visitor
    from picamera import PiCamera #importing the camera
    print("Button pressed")
    camera = PiCamera()
    camera.rotation = 180
    camera.capture(file_path+file_name) #capturing the image
    print("Photo Taken")
    uploadToS3(file_path, file_name, BUCKET, location) #uploading the image of the visitor to s3 bucket
    print('Detected faces for')
    facialFeatures = "Hello, This is HAY Smart Home Service.\nThere is a visitor at your door" #Starting the email string here
    for faceDetail in detect_faces(BUCKET, file_name):
        facialFeatures += "Age Range Of Visitor: "+ str(faceDetail['AgeRange']['Low']) + "-"
        facialFeatures += str(faceDetail['AgeRange']['High']) + "\n"
        facialFeatures += "Gender Of Visitor: "+ str(faceDetail['Gender']['Value']) + ": "
        facialFeatures += str(faceDetail['Gender']['Confidence'])
        print('Here are the other attributes:')
        print(json.dumps(faceDetail, indent=4, sort_keys=True))
    print(facialFeatures)
    facialFeatures+="\nYou can view a picture of the visitor below: \n" + "https://hay-iot.s3.amazonaws.com/"+file_name
    pub_facial.sendFeatures(facialFeatures) #sending the email message to the function that will publish to topic to send to email

def uploadToS3(file_path, file_name, bucket_name, location):
    s3 = boto3.resource('s3')  # Create an S3 resource
    exists = True

    try:
        s3.meta.client.head_bucket(Bucket=bucket_name)
    except botocore.exceptions.ClientError as e:
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            exists = False

    if exists == False:
        s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)

    # Upload the file
    full_path = file_path + "/" + file_name
    s3.Object(bucket_name, file_name).put(Body=open(full_path, 'rb'))
    print("File uploaded")


def detect_labels(bucket, key, max_labels=10, min_confidence=90, region="us-east-1"):
    rekognition = boto3.client("rekognition", region)
    response = rekognition.detect_labels(
        Image={
            "S3Object": {
                "Bucket": bucket,
                "Name": key,
            }
        },
        MaxLabels=max_labels,
        MinConfidence=min_confidence,
    )
    return response['Labels']


def detect_faces(bucket, key, max_labels=10, min_confidence=90, region="us-east-1"):
    rekognition = boto3.client("rekognition", region)
    response = rekognition.detect_faces(
        Image={
            "S3Object": {
                "Bucket": bucket,
                "Name": key,
            }
        },
        Attributes=['ALL']
    )
    return response['FaceDetails']

def buttonRelease():
    print("Button release")


def checkButton():
    button.when_pressed = takePhoto
    button.when_released  = buttonRelease
    
