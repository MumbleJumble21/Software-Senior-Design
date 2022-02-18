import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
p = GPIO.PWM(12, 50)
p.start(11.5)
print ("start wait 15 seconds for actuator to settle")
time.sleep(15)
print ("actuator ready")
dc = 11.5
while True:

    key = input ("enter i for in or o out " )
    
    if key == "i":
        dc = dc - 0.1
    
    elif key == "o":
        dc = dc + 0.1
    
    else:
        print (" i or o only")


    p.ChangeDutyCycle(dc)
    print (" dc value = ",dc)