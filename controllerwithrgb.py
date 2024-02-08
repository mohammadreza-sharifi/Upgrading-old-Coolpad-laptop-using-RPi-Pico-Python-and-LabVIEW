from machine import UART
from machine import Pin as pin
from time import sleep
import machine, neopixel

#####
#thanks to microsoft copilot for guiding me to write these functions to control RGB LED ring using neopixel library
# Pin number, number of LEDs, and bpp
PIN_NUM = 15
NUM_LEDS = 16
BPP = 4

# Create a neopixel object
np = neopixel.NeoPixel(machine.Pin(PIN_NUM), NUM_LEDS, bpp=BPP)

# Define the rainbow colors
RED = (255, 0, 0, 128)
ORANGE = (255, 128, 0, 128)
YELLOW = (255, 255, 0, 128)
GREEN = (0, 255, 0, 128)
BLUE = (0, 0, 255, 128)
INDIGO = (75, 0, 130, 128)
VIOLET = (148, 0, 211, 128)

# Store the colors in a list
COLORS = [RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET]

# Loop through the colors and display them on the LEDs
def rainbow():
    for color in COLORS:
            # Set the color of each pixel
        for i in range(NUM_LEDS):
            np[i] = color
            # Write the data to the LEDs
        np.write()
           
        time.sleep(0.5)


def disable_rainbow():
    for color in COLORS:
            # Set the color of each pixel
        for i in range(NUM_LEDS):
            np[i] = (0, 0, 0, 0)
            # Write the data to the LEDs
        np.write()

#####
ut = UART(0,9600)

command = b'S'

#Define Driver pins
in1 = pin(16,pin.OUT)
in3 = pin(17,pin.OUT)


#########
ENA = pin(18,pin.OUT)
ENB = pin(19,pin.OUT)

ENA.value(1)
ENB.value(1)
#########

def enable_fan():
    in1.value(1)
    in3.value(1)


def disable_fan():
    in1.value(0)
    in3.value(0)


disable_fan()

while True:
  
    if ut.any():
        command = ut.readline()
        #print(command)     
        
        if command == b's':
            disable_fan()
            
        elif command == b'o':
            enable_fan()
            rainbow()
            
        elif command == b'f':
            disable_fan()
            disable_rainbow()
                       
        else:
            pass

