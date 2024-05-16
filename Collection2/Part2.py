from pathlib import Path
import sys
from gpiozero import PWMLED
import time

HERE = Path(__file__).parent.parent
sys.path.append(str(HERE / 'Common'))
from ADCDevice import * 

USING_GRAVITECH_ADC = False

RED = PWMLED(17)
YELLOW = PWMLED(27)
GREEN = PWMLED(22)
BLUE = PWMLED(18)
ADC = ADCDevice()

def setup():
    global ADC
    if(ADC.detectI2C(0x48) and USING_GRAVITECH_ADC): 
        ADC = GravitechADC()
    elif(ADC.detectI2C(0x48)): # Detect the pcf8591.
        ADC = PCF8591()
    elif(ADC.detectI2C(0x4b)): # Detect the ads7830
        ADC = ADS7830()
    else:
        print("No correct I2C address found, \n"
            "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
            "Program Exit. \n")
        exit(-1)

def loop():
    while True:
        value = ADC.analogRead(0)    # read the ADC value of channel 0
        percentage = (value / 255) * 100  # calculate the voltage value
        print(f'ADC Value: {value} \tPercentage: {percentage:.0f}%')
        time.sleep(0.1)
        if percentage >= 1 and percentage < 25:
            RED.off()
            YELLOW.off()
            GREEN.off()
            BLUE.off()
        elif percentage >= 25 and percentage < 50:
            RED.off()
            YELLOW.off()
            GREEN.off()
            BLUE.on()
        elif percentage >= 50 and percentage < 75:
            RED.off()
            YELLOW.off()
            GREEN.on()
            BLUE.on()
        elif percentage >= 75 and percentage < 95:
            RED.off()
            YELLOW.on()
            GREEN.on()
            BLUE.on()
        else:
            RED.on()
            YELLOW.on()
            GREEN.on()
            BLUE.on()
        
        if percentage == 0:
            RED.off()
            YELLOW.off()
            GREEN.off()
            BLUE.off()

def destroy():
    global RED, YELLOW, GREEN, BLUE, ADC
    RED.close()
    YELLOW.close()
    GREEN.close()
    BLUE.close()
    ADC.close()
    
if __name__ == '__main__':   # Program entrance
    print ('Program is starting ... ')
    try:
        setup()
        loop()
    except KeyboardInterrupt: # Press ctrl-c to end the program.
        destroy()