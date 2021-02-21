# raindrop sensor DO connected to GPIO18
# HIGH = no rain, LOW = rain detected
# Buzzer on GPIO13
from time import sleep
from turn_90 import *
from pub_temp import *
from button_face_recognition import *
from pub_rain_detected import *
from pub_sub_sign import *
from sub_rain import *
import subscription 
import remove_txt 





 

# Rain, send alert, temp, humid, lcd, button to send email

def smart_home():   #Here is the function to detect the rain

    subscription.subAll()  #From subscription.py, purpose is to perform all the functions that subscribe to topics

    while True:
        rain = getRain()   #In the pub_rain_detected, configures the GPIO
        submit_temp()   #From pub_temp.py 
                        #This function publishes values like temperature and humidity onto topic for the dynano db
                        # for the graph                    


        if (rain == 0):  #check for rain
            print("It's raining, hide!")
            rain_detected()   #From pub_ravncin_detected.py 
                              #This will only activate if there is rain detected. Once it runs, it will send an alert via email to users and will also close the windows 
                              
        
        sign()                #From pub_sub_sign.py, waits for the message from web server then publish to a new topic for the web server to display
  
        sleep(5)
      


def main():
    print("\n\nHello Handsome, Smart home is activated\n")

    remove_txt.remove()

    smart_home()



if __name__== "__main__" :
    main()