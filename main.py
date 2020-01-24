import sys
import json
import RPi.GPIO as GPIO
from nav.dc.dc_motion import DC_Motion

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

    motion.mov(True, 5, GPIO)

    GPIO.cleanup()

if __name__ == "__main__":
    main()
