import time
from .misc import *
from .dc_constants import *
import math

class DC_Motion:
    def __init__(self, config, GPIO):
        # Each wheel in a DC motor has two pins. Set both as output pins
        self.wheels = config["motor_pins"]
        for _, pins in self.wheels.items():
            GPIO.setup(pins[0], GPIO.OUT)
            GPIO.setup(pins[1], GPIO.OUT)

        # Rotary pins. Set as input pins
        self.rotary_pins = config["rotary_pins"]
        for rotary, pin in self.rotary_pins.items():
            if rotary != "DC_rotary_S":
                GPIO.setup(pin, GPIO.IN)

        # Encoder pins. Set as output pins
        self.encoders = config["encoder_pins"]
        for _, pin in self.encoders.items():
            GPIO.setup(pin, GPIO.OUT)

        # Controls wheel speed fwd and backward
        for _, pin in self.encoders.items():
            GPIO.output(pin, True)

        clear_wheels(config["motor_pins"], GPIO)

        # Count ticks off the rotary encoder
        self.global_counter = 0

        # NOT USING RoSPin
        # GPIO.add_event_detect(config["rotary_pins"]["DC_rotary_C"], GPIO.FALLING, callback="clear")

    def _rotary_deal(self, GPIO):
        prev_rotary_b = GPIO.input(self.rotary_pins['DC_rotary_B'])
        flag = 0

        # TODO: Fail safe if hardware fails and current rotary b is not set.
        while not GPIO.input(self.rotary_pins['DC_rotary_A']):
            current_rotary_b = GPIO.input(self.rotary_pins['DC_rotary_B'])
            flag = 1

        if flag == 1:
            flag = 0
            if prev_rotary_b == 0 and current_rotary_b == 1:
                self.global_counter += 1
            else:
                self.global_counter -= 1

    def mov(self, dir: bool, distance: int, GPIO):
        distance = int(round(distance * rotation_constant / (wheels_diameter*math.pi)))

        if dir:
            while abs(self.global_counter) < distance:
                # Controls direction
                for _, pins in self.wheels.items():
                    GPIO.output(pins[0], True)
                    GPIO.output(pins[1], False)

                self._rotary_deal(GPIO)
        else:
            while abs(self.global_counter) < distance:
                # Controls direction
                for _, pins in self.wheels.items():
                    GPIO.output(pins[0], False)
                    GPIO.output(pins[1], True)

                self._rotary_deal(GPIO)

        clear_wheels(self.wheels, GPIO)
        self.global_counter = 0

    # TODO: Calculate degrees turned using magnetometer
    def strafe(self, dir: bool, degrees: int, GPIO):
        if dir:
            turn_wheels = [self.wheels["DC_FR"][1], self.wheels["DC_FL"][0], self.wheels["DC_BL"][0], self.wheels["DC_BR"][1]]
            non_turn_wheels = [self.wheels["DC_FR"][0], self.wheels["DC_FL"][1], self.wheels["DC_BL"][1], self.wheels["DC_BR"][0]]
        else:
            turn_wheels = [self.wheels["DC_FR"][0], self.wheels["DC_FL"][1], self.wheels["DC_BL"][1], self.wheels["DC_BR"][0]]
            non_turn_wheels = [self.wheels["DC_FR"][1], self.wheels["DC_FL"][0], self.wheels["DC_BL"][0], self.wheels["DC_BR"][1]]

        for a, b in zip(turn_wheels, non_turn_wheels):
            GPIO.output(a, True)
            GPIO.output(b, False)
            
        time.sleep(1)

        clear_wheels(self.wheels, GPIO)

    # TODO: Calculate distance strafed using onboard sensors
    def turn(self, dir:bool, distance: int, GPIO):
        if dir:
            turn_wheels = [self.wheels["DC_FR"][1], self.wheels["DC_FL"][0], self.wheels["DC_BL"][1], self.wheels["DC_BR"][0]]
            non_turn_wheels = [self.wheels["DC_FR"][0], self.wheels["DC_FL"][1], self.wheels["DC_BL"][0], self.wheels["DC_BR"][1]]
        else:
            turn_wheels = [self.wheels["DC_FR"][0], self.wheels["DC_FL"][1], self.wheels["DC_BL"][0], self.wheels["DC_BR"][1]]
            non_turn_wheels = [self.wheels["DC_FR"][1], self.wheels["DC_FL"][0], self.wheels["DC_BL"][1], self.wheels["DC_BR"][0]]

        for a, b in zip(turn_wheels, non_turn_wheels):
            GPIO.output(a, True)
            GPIO.output(b, False)

        # Distance calculation and stop movement here
        time.sleep(1)

        clear_wheels(self.wheels, GPIO)
