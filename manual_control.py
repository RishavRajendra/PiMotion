import keyboard
import time
import sys
import json
import RPi.GPIO as GPIO
from nav.dc.dc_motion import DC_Motion

# Refering to pins by the "Broadcom SOC channel".
GPIO.setmode(GPIO.BCM)

with open('config.json') as data:
    config = json.load(data)

motors_select = config['motors']

if motors_select == "DC":
    motion = DC_Motion(config["dc_config"], GPIO)
elif motors_select == "stepper":
    pass
else:
    raise ValueError("Motors not selected in config.json")
    sys.exit()

listening = True
while listening:
    if keyboard.is_pressed('x'):
        listening = False
        print("Stopping")
    elif keyboard.is_pressed('w'):
        # forward
        motion.mov(True, 5, GPIO)
        print("forward")
    elif keyboard.is_pressed('s'):
        # backwards
        motion.mov(False, 5, GPIO)
        print("backwards")
    elif keyboard.is_pressed('q'):
        # turn left
        motion.turn(True, 5, GPIO)
        print("turning left")
    elif keyboard.is_pressed('e'):
        # turn right
        motion.turn(False, 5, GPIO)
        print("turning right")
    elif keyboard.is_pressed('a'):
        #strafe right
        pass
    elif keyboard.is_pressed('d'):
        #strafe left
        pass
    time.sleep(.2)
    
GPIO.cleanup()