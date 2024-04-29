from gpiozero import RGBLED, Button
import time
import random

# active_high must be true because it is a common anode RGBLed
LED = RGBLED(red=17, green=18, blue=27, active_high=True)
BUTTON = Button(23)
is_blinking = True

def set_color(r, g, b):
    """ Invert the colors due to using a common anode """
    LED.color = (1 - r, 1 - g, 1 - b)

def initial_test():
    set_color(1, 0, 0)
    print("All red")
    time.sleep(1)
    set_color(0, 1, 0)
    print("All green")
    time.sleep(1)
    set_color(0, 0, 1)
    print("All blue")
    time.sleep(1)


def changeLedState():
    global is_blinking
    is_blinking = not is_blinking

def destroy():
    LED.close()

if __name__ == '__main__':  # Program entrance
    print('Program is starting ... ')
    try:
        BUTTON.when_activated = changeLedState
        while True:
            initial_test()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
