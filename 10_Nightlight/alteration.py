# Description : Control LED with Photoresistor
from pathlib import Path
import sys
from gpiozero import LEDBarGraph
import time

HERE = Path(__file__).parent.parent
sys.path.append(str(HERE / 'Common'))
from ADCDevice import * 

USING_GRAVITECH_ADC = False # Only modify this if you are using a Gravitech ADC

LED = LEDBarGraph(17, 18, 27, 22, 23, 24, 25, 16, 20, 12)
ADC = ADCDevice() # Define an ADCDevice class object

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
    global ADC, LED
    while True:
        value = ADC.analogRead(0)   # read the ADC value of channel 0

        for i in range(1, 10):
            if value >= (255 / 10 * i):
                LED[i-1].off()
            else:
                LED[i].on()
    
        voltage = value / 255.0 * 3.3
        print (f'ADC Value: {value} \tVoltage: {voltage:.2f} \tLED Value: {LED.value:.2f}')
        time.sleep(0.01)

def destroy():
    global ADC, LED
    ADC.close()
    LED.close()
    
if __name__ == '__main__':   # Program entrance
    print ('Program is starting... ')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()