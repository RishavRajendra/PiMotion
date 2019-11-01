import math
# Stepper mode select
STEPPER_m0 = 17
STEPPER_m1 = 27
STEPPER_m2 = 22

STEP_MODE_SELECT = [STEPPER_m0, STEPPER_m1, STEPPER_m2]

# First wheel GPIO Pin
BR_step = 21
BR_dir = 20

# Second wheel GPIO Pin
FR_step = 11
FR_dir = 10

# Third wheel GPIO Pin
BL_step = 7
BL_dir = 8

# Fourth wheel GPIO Pin
FL_step = 24
FL_dir = 23

# Direction constants
FWD = True
REV = False

# Clockwise and Counter-clockwise constants 
CW = 1 			                 
CCW = 0

# whole, 1/2, 1/4, and 1/8 steps per revolution constants.
# steps per revolution is obtained by (360/1.8) * denominator. 
# ie: (360/1.8) * 2 = 400 for half steps per revolution
STEPS_PER_REVOLUTION = {'whole': 200, 'half': 400, 'quarter': 800,'eighth': 1600}

DISTANCE = 60*math.pi/25.4

# individual steps per inch based off of whole step, 1/2 step, 1/4 step, and 1/8 step.

STEPS_PER_INCH = {'whole'  : STEPS_PER_REVOLUTION['whole']    / DISTANCE,
                  'half'   : STEPS_PER_REVOLUTION['half' ]    / DISTANCE,
                  'quarter': STEPS_PER_REVOLUTION['quarter']  / DISTANCE,
                  'eighth' : STEPS_PER_REVOLUTION['eighth' ]  / DISTANCE }

#STEPS_PER_INCH_STRAFE = STEPS_PER_REVOLUTION/(DISTANCE*0.9)  # Calibrates steps_per_inch for strafe motion.

STEPS_PER_INCH_STRAFE = {'whole'  : STEPS_PER_REVOLUTION['whole']   / (DISTANCE*0.9)
                         'half'   : STEPS_PER_REVOLUTION['half' ]   / (DISTANCE*0.9)
                         'quarter': STEPS_PER_REVOLUTION['quarter'] / (DISTANCE*0.9)
                         'eighth' : STEPS_PER_REVOLUTION['eighth' ] / (DISTANCE*0.9) }
