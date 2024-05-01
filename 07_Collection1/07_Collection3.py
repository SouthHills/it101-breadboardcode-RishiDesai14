from gpiozero import RGBLED, Button
import time
import random
from signal import pause

# active_high must be true because it is a common anode RGBLed
LED = RGBLED(red=17, green=18, blue=27, active_high=True)
BUTTON = Button(23)
game_started = False

def set_color(r, g, b):
    """ Invert the colors due to using a common anode """
    LED.color = (1 - r, 1 - g, 1 - b)

def start_game():
    global game_started
    while True:
        if game_started:
            random_color = random.choice([(1, 0, 0), (0, 1, 0), (0, 0, 1)])
            set_color(*random_color)
            time.sleep(1)

def end_game(is_winner):
    if is_winner:
        for _ in range(5): # Green
            set_color(0, 1, 0)
            time.sleep(0.5)
            set_color(0, 0, 0)
            time.sleep(0.5)
    else:
        for _ in range(5): # Red
            set_color(1, 0, 0)
            time.sleep(0.5)
            set_color(0, 0, 0)
            time.sleep(0.5)
    destroy()
    exit()

def button_pressed():
    global game_started
    print("Button pressed")
    if not game_started:
        game_started = True
    else:
        game_started = False
        if LED.color == (1, 0, 1):
            end_game(True)
        else:
            end_game(False)

def destroy():
    LED.close()

if __name__ == '__main__':  # Program entrance
    print('Program is starting ... ')
    try:
        BUTTON.when_pressed = button_pressed
        start_game()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
