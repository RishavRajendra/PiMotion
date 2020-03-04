import time
import sys
import json
import RPi.GPIO as GPIO
from nav.dc.dc_motion import DC_Motion
from sensor.ultrasonic import get_distance

# Test for robot to move forward
# 5 in, 12 in, 25 in. 50 in
def mov_fwd_test(x):
    distance_first = get_distance("fwd", config, GPIO)
    motion.mov(True, x, GPIO)
    distance_second = get_distance("fwd", config, GPIO)
    distance_moved_sensor = distance_second - distance_first
    error_margin = x - distance_moved_sensor
    print(f"[TEST] Move fwd -> Distance: {x}, Sensor: {distance_moved_sensor}, Error: {error_margin}" )

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

    mov_fwd_test(12)

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
