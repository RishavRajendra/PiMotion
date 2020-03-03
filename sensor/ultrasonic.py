import time

def get_distance(direction, config, GPIO):
    ultrasonic_pins = {
        "fwd": config["front_ultrasonic"],
        "left": config["left_ultrasonic"],
        "right": config["right_ultrasonic"]
    }

    trig, echo = ultrasonic_pins[direction]

    GPIO.setup(trig, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)

    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)

    while GPIO.input(echo)==0:
        pulse_start = time.time()

    while GPIO.input(echo)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150 * 0.393701

    distance = round(distance,2)

    return distance
