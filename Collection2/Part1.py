from gpiozero import PWMLED
import subprocess
import time

# Pin numbers for the LEDs
RED = PWMLED(18)
GREEN = PWMLED(23)


def is_internet_connected():
    try:
        # Run the ping command with a timeout of 2 seconds and count 1 packet
        subprocess.check_output(['ping', '-c', '1', '-W', '2', 'www.google.com'])
        return True
    except subprocess.CalledProcessError:
        return False

def destroy():
    RED.close()
    GREEN.close()

if __name__ == '__main__':
    try:
        while True:
            if is_internet_connected():
                GREEN.on()
            else:
                GREEN.off()
                RED.on()
            time.sleep(5)

    except KeyboardInterrupt:
        destroy()