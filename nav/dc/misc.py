# set output of all wheels as FALSE.
# wheels: Expects pin numbers of all wheels as a dict. See config for details
def clear_wheels(wheels, GPIO):
    for _, pins in wheels.items():
        GPIO.output(pins[0], False)
        GPIO.output(pins[1], False)
