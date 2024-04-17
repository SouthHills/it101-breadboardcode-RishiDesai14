from gpiozero import LED as LEDClass, Button
from signal import pause
import time

LED = LEDClass(17)  # define ledPin
BUTTON = Button(18)  # define buttonPin
is_blinking = False

def changeLedState():
    global LED
    if is_blinking == True:
        LED.on()
        time.sleep(.5)
        LED.off()
        time.sleep(.5)
    else:
        LED.off()

def change_blinking():
    global is_blinking
    is_blinking = not is_blinking

def destroy():
    global LED, BUTTON
    # Release resources
    LED.close()
    BUTTON.close()

if __name__ == "__main__":     # Program entrance
    print ("Program is starting...")
    try:
        BUTTON.when_pressed = change_blinking
        while True:
            changeLedState()
        
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()