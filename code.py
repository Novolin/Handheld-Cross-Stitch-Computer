# Cross Stitch Visual Display
# V0.0 - Jan 31, 2024


import busio
import board 
import digitalio
from adafruit_rgb_display import color565
import adafruit_rgb_display.ili9341 as ili9341
import time
import asyncio

spi = busio.SPI(board.GP14, MOSI=board.GP15, MISO=board.GP12)
display = ili9341.ILI9341(spi, cs=digitalio.DigitalInOut(board.GP13),
    dc=digitalio.DigitalInOut(board.GP17),
    rst = digitalio.DigitalInOut(board.GP16))
display.fill(color565(0xff, 0x11, 0x22))
display.pixel(120, 160, 0)

class Button:
    def __init__(self, pin):
        self.pin = digitalio.DigitalInOut(pin)
        self.pin.direction = digitalio.INPUT_PULLUP
        
