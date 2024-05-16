from gpiozero import RGBLED

LED = RGBLED(red=17, green=18, blue=27, active_high=True)

def cpu_temperature():
    file = open('/sys/class/thermal/thermal_zone0/temp')
    readFile = float(file.read()) / 1000
    return readFile


def set_color(r, g, b):
    """ Invert the colors due to using a common anode """
    LED.color = (1 - r, 1 - g, 1 - b)

def light_indicator(cpu_temp):
    if cpu_temp < 15000.0:
        set_color(0, 0, 1)
    elif cpu_temp >= 80000.0:
        set_color(1, 0, 0)

if __name__ == "__main__":
    getTemp = cpu_temperature()
    getLight = light_indicator(getTemp)