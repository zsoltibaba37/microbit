#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from microbit import *

# init pwm value
pwm = 500
text = "PWM:50%"
display.scroll(str(text), delay=100)
display.clear()

def bargraph(p):
    """
    :param p: internal pwm value
    """
    BarValue = ((p * 25) // 1000)
    BarRest = BarValue % 5

    if p <= 250:
        for i in range(0, BarRest):
            display.set_pixel(i, 4, 5)
    elif p >= 250 and p < 500:
        for y in range(4, 3, -1):
            for x in range(0, 5):
                display.set_pixel(4-x, y, 9)
        for i in range(0, BarRest):
            display.set_pixel(i, 0, 6)
    elif p >= 500 and p < 750:
        for y in range(4, 2, -1):
            for x in range(0, 5):
                display.set_pixel(4-x, y, 9)
        for i in range(0, BarRest):
            display.set_pixel(i, 0, 6)
    elif p >= 750 and p < 1000:
        for y in range(4, 1, -1):
            for x in range(0, 5):
                display.set_pixel(4 - x, y, 9)
        for i in range(0, BarRest):
            display.set_pixel(i, 0, 6)
    elif p == 1000:
        for y in range(4, 0, -1):
            for x in range(0, 5):
                display.set_pixel(4 - x, y, 9)


while True:
    if button_a.get_presses():
        display.clear()
        pwm -= 20
        if pwm <= 0:
            pwm = 0
            pin0.write_analog(pwm)
        else:
            pin0.write_analog(pwm)

    if button_b.get_presses():
        display.clear()
        pwm += 20
        if pwm >= 1000:
            pwm = 1000
            pin0.write_analog(pwm)
        else:
            pin0.write_analog(pwm)

    bargraph(pwm)


