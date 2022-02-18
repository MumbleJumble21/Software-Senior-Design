
# Package imports.
from evdev import InputDevice, categorize, ecodes # Measures specified Linux input devices being broadcasted in '/dev/input'. Used to interface Bluetooth controller.
from PCA9685 import PCA9685 # Proprietary library needed to get specific servo HAT used in this year's project.

# Initialize PCA9685 library as object.
pwm = PCA9685()

# Set PWMFreq that servos will respond to (requires math, your value will most likely be different. See your servo product specs for provided PWM formula!)
pwm.setPWMFreq(50)

# For this specific HAT, all pulses had to be "initalized" with a zero value before they could be used.
pwm.setServoPulse(0,0)
pwm.setServoPulse(4,0)
pwm.setServoPulse(8,0)
pwm.setServoPulse(12,0)

# Specify input device we will be listening to by pointing to event "file".
device = InputDevice('/dev/input/event6')
print("Beep boop! You are using device:", device)

# Calculated PWM pulse values that make the robot move in set direction.
full_backward = 10
half_backward = 50
per_backward = 65
full_forward = 150
half_forward = 100
per_forward = 125

# PWM will only pulse once, to keep the signal constant we need to put in a loop. Event "codes" can be found in documentation of evdev library.
while True:
    for event in device.read_loop():

        if(event.code == 17):
            if(event.value == -1):
                '''Forward movement, 0 and 4 get 150 for normal forward
                    and 8 and 12 get 10 for backward movement since they have
                    a gear atached to them
                '''
                pwm.setRotationAngle(0,per_forward)
                pwm.setRotationAngle(8,per_backward)
            if(event.value == 0):
                '''No movement'''
                pwm.setRotationAngle(0,0)
                pwm.setRotationAngle(8,0)
            if(event.value == 1):
                '''Forward movement, 0 and 4 get 10 for normal backward
                    and 8 and 12 get 10 for forward movement since they have
                    a gear atached to them
                '''
                pwm.setRotationAngle(0,per_backward)
                pwm.setRotationAngle(8,per_forward)
        if(event.code == 16):
            if(event.value == -1):
                '''Turning Left'''
                pwm.setRotationAngle(0,full_backward)
                pwm.setRotationAngle(8,full_backward)
            if(event.value == 0):
                '''No movement'''
                pwm.setRotationAngle(0,0)
                pwm.setRotationAngle(4,0)
                pwm.setRotationAngle(8,0)
                pwm.setRotationAngle(12,0)
            if(event.value == 1):
                '''Turning right'''
                pwm.setRotationAngle(0,full_forward)
                pwm.setRotationAngle(8,full_forward)
        if(event.type == ecodes.EV_MSC):
                '''Detect A, B, X, Y buttons'''
                if(event.code  == 4):
                        if(event.value == 589825):
                                '''A key moves conveyor belt backwards'''
                                pwm.setRotationAngle(4,full_backward)
                        if(event.value == 589826):
                                '''B key rotates moves delivery tray down'''
                                pwm.setRotationAngle(12,full_backward)
                        if(event.value == 589828):
                                '''X key rotates conveyor belt forwards'''
                                pwm.setRotationAngle(4,full_forward)
                        if(event.value == 589829):
                                '''Y key moves delivery tray up'''
                                pwm.setRotationAngle(12,full_forward)
        if(event.type == ecodes.EV_KEY):
                if(event.code == 304):
                        if(event.value == 0):
                                '''Stopping A key press'''
                                pwm.setRotationAngle(4,0)
                if(event.code == 305):
                        if(event.value == 0):
                                '''Stopping B key press'''
                                pwm.setRotationAngle(12,0)
                if(event.code == 307):
                        if(event.value == 0):
                                '''Stopping X key press'''
                                pwm.setRotationAngle(4,0)
                if(event.code == 308):
                        if(event.value == 0):
                                '''Stopping Y key press'''
                                pwm.setRotationAngle(12,0)

        if(event.type == ecodes.EV_ABS):
                if(event.code == 10):
                        if(event.value == 1023):
                                print("Left trigger down")
                                pwm.setRotationAngle(3,50)
                                pwm.setRotationAngle(7,50)
                                pwm.setRotationAngle(11,50)
                                pwm.setRotationAngle(15,50)
                        if(event.value == 0):
                                pwm.setRotationAngle(3,0)
                                pwm.setRotationAngle(7,0)
                                pwm.setRotationAngle(11,0)
                                pwm.setRotationAngle(15,0)
                if(event.code == 9):
                        if(event.value == 1023):
                                print("Right trigger down")
                                pwm.setRotationAngle(3,100)
                                pwm.setRotationAngle(7,100)
                                pwm.setRotationAngle(11,100)
                                pwm.setRotationAngle(15,100)
                        if(event.value ==0):
                                pwm.setRotationAngle(3,0)
                                pwm.setRotationAngle(7,0)
                                pwm.setRotationAngle(11,0)
                                pwm.setRotationAngle(15,0)