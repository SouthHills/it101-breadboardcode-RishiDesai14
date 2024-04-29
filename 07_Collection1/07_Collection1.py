from gpiozero import Button
from signal import pause
import subprocess

FIRE_BUTTON = Button(18)
CHROM_BUTTON = Button(23)

firefox_process = None
chromium_process = None

def launch_firefox():
    global firefox_process
    if firefox_process is None:
        firefox_process = subprocess.Popen(["firefox"])
    else:
        firefox_process.terminate()
        firefox_process = None

def launch_chromium():
    global chromium_process
    if chromium_process is None:
        # Check if chromium is available, otherwise try chromium-browser
        try:
            chromium_process = subprocess.Popen(["chromium"])
    
        except FileNotFoundError:
            chromium_process = subprocess.Popen(["chromium-browser"])

    else:
        chromium_process.terminate()
        chromium_process = None

def destroy():
    global FIRE_BUTTON, CHROM_BUTTON
    FIRE_BUTTON.close()
    CHROM_BUTTON.close()

if __name__ == "__main__":

    try:
        FIRE_BUTTON.when_pressed = launch_firefox
        CHROM_BUTTON.when_pressed = launch_chromium
        pause()
    except:
        destroy()