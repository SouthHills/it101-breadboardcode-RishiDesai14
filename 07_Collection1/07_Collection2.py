from gpiozero import LED
import time

RED_LED = LED(18)
YELLOW_LED = LED(23)
GREEN_LED = LED(24)


def initial_test():
    global RED_LED, YELLOW_LED, GREEN_LED

    RED_LED.on()

    while True:
        time.sleep(5)
        RED_LED.off()
        GREEN_LED.on()
        time.sleep(7)
        GREEN_LED.off()
        YELLOW_LED.on()
        time.sleep(2)
        RED_LED.on()
        YELLOW_LED.off()
        GREEN_LED.off()

def destroy():
    RED_LED.off()
    YELLOW_LED.off()
    GREEN_LED.off()


if __name__ == "__main__":
    try:
        initial_test()
    except:
        destroy()