#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

from microbit import *

# PWM start with ~50%
pwm = 500

# Send analod signal to the P0 port
pin0.write_analog(pwm)

# Bar graph Dictionary
bar_graph = {0:Image("00000:00000:00000:00000:00000"),
             1:Image("00000:00000:00000:00000:00900"),
             2:Image("00000:00000:00000:00000:09990"),
             3:Image("00000:00000:00000:00000:99999"),
             4:Image("00000:00000:00000:00900:99999"),
             5:Image("00000:00000:00000:09990:99999"),
             6:Image("00000:00000:00000:99999:99999"),
             7:Image("00000:00000:00900:99999:99999"),
             8:Image("00000:00000:09990:99999:99999"),
             9:Image("00000:00000:99999:99999:99999"),
             10:Image("00000:00900:99999:99999:99999"),
             11:Image("00000:09990:99999:99999:99999"),
             12:Image("00000:99999:99999:99999:99999"),
             13:Image("00900:99999:99999:99999:99999"),
             14:Image("09990:99999:99999:99999:99999"),
             15:Image("99999:99999:99999:99999:99999")}

# This is handle the A and the B button
while True:
    if button_a.get_presses():
        pwm -= 50
        if pwm <= 0:
            pwm = 0
            pin0.write_analog(pwm)
        else:
            pin0.write_analog(pwm)

    elif button_b.get_presses():
        pwm += 50
        if pwm >= 1023:
            pwm = 1023
            pin0.write_analog(pwm)
        else:
            pin0.write_analog(pwm)

    blist_Value = ((pwm * 16) // 1024) # Scales the analog signal to the bar graph
    display.show(bar_graph[blist_Value])
