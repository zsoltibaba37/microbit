#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from microbit import *

# Initial pwm value
pwm = 500

# Writes analog signal on the P0 leg
pin0.write_analog(pwm)
text = "PWM=50%"
display.scroll(str(text), delay=100)
display.clear()


# Bar Graph function
def bargraph(p):
    """
    :param p: internal pwm value
    """
    barvalue = (p * 20) // 1000
    barrest = barvalue % 5

    if p <= 250:
        for i in range(0, barrest):
            display.set_pixel(i, 4, 6)
    elif 250 <= p < 500:
        for y in range(4, 3, -1):
            for x in range(0, 5):
                display.set_pixel(4 - x, y, 9)
        for i in range(0, barrest):
            display.set_pixel(i, 0, 6)
    elif 500 <= p < 750:
        for y in range(4, 2, -1):
            for x in range(0, 5):
                display.set_pixel(4 - x, y, 9)
        for i in range(0, barrest):
            display.set_pixel(i, 0, 6)
    elif 750 <= p < 1000:
        for y in range(4, 1, -1):
            for x in range(0, 5):
                display.set_pixel(4 - x, y, 9)
        for i in range(0, barrest):
            display.set_pixel(i, 0, 6)
    elif p >= 1000:
        for y in range(4, 0, -1):
            for x in range(0, 5):
                display.set_pixel(4 - x, y, 9)


# Status led BOOL
s = False

# Run forever
while True:
    if button_a.get_presses():
        display.clear()
        pwm -= 50
        if pwm <= 0:
            pwm = 0
        else:
            pin0.write_analog(pwm)
        bargraph(pwm)
    if button_b.get_presses():
        display.clear()
        pwm += 50
        if pwm >= 1023:
            pwm = 1023
        else:
            pin0.write_analog(pwm)
        bargraph(pwm)
    else:
        bargraph(pwm)

    # Status led in x=4 y=0 position
    if s is False:
        display.set_pixel(4, 0, 8)
        sleep(pwm // 10)
        s = True
    elif s is True:
        display.set_pixel(4, 0, 0)
        sleep(pwm // 10)
        s = False
