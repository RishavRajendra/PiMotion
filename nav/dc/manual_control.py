import dc_motion
import keyboard
import time
import RPi.GPIO as GPIO

while not keyboard.is_pressed('x'):
    if keyboard.is_pressed('w'):
        # forward
        dc_motion.mov(True, 5, GPIO)
    elif keyboard.is_pressed('s'):
        # backwards
        dc_motion.mov(False, 5, GPIO)
    elif keyboard.is_pressed('q'):
        # turn left
        dc_motion.turn(True, 5, GPIO)
    elif keyboard.is_pressed('e'):
        # turn right
        dc_motion.turn(True, 5, GPIO)
    elif keyboard.is_pressed('a'):
        #strafe right
    elif keyboard,is_pressed('d'):
        #strafe left 
    time.sleep(.2)