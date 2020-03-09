import time
import sys
import json
import RPi.GPIO as GPIO
from nav.dc.dc_motion import DC_Motion
from sensor.ultrasonic import get_distance

# Test for robot to move forward
# 5 in, 12 in, 25 in. 50 in
#if percentage error is +ve, the actual move lags behind the asked mov, if -ve gains more distance than asked
def mov_fwd_test(*args):
    for x in args:
        distance_first = get_distance("fwd", config, GPIO)
        if x <= distance_first:
            motion.mov(True, x, GPIO)
            distance_second = get_distance("fwd", config, GPIO)
            distance_moved_sensor = distance_first - distance_second
            error_percentage = ((x - distance_moved_sensor)/x)*100
            print(f"[TEST] Move fwd -> DistanceForward: {x}, Sensor: {distance_moved_sensor}, ErrorPercentage: {error_percentage}" )
        '''else:
            motion.mov(False, x, GPIO)
            distance_second = get_distance("fwd", config, GPIO)
            distance_moved_sensor = distance_second - distance_first
            error_percentage = ((x - distance_moved_sensor)/x)*100
            print(f"[TEST] Move fwd -> DistanceBackward: {x}, Sensor: {distance_moved_sensor}, ErrorPercentage: {error_percentage}" ) 
        ''' 

def main():
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

    mov_fwd_test(4,10, 7, 12)

    # Example for fwd ultrasonic sensor
    """
    print("Ultrasonic fwd")
    distance_fwd = get_distance("fwd", config, GPIO)
    print(f"Distance fwd = {distance_fwd}")
    print("Ultrasonic left")
    distance_left = get_distance("left", config, GPIO)
    print(f"Distance left = {distance_left}")
    print("Ultrasonic right")
    distance_right = get_distance("right", config, GPIO)
    print(f"Distance right = {distance_right}")
"""
if __name__ == "__main__":
    main()
