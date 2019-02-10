#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

from microbit import *

pwm = 500

pin0.write_analog(pwm)

bar01 = Image("00000:00000:00000:00000:00000")
bar02 = Image("00000:00000:00000:00000:00900")
bar03 = Image("00000:00000:00000:00000:09990")
bar04 = Image("00000:00000:00000:00000:99999")
bar05 = Image("00000:00000:00000:00900:99999")
bar06 = Image("00000:00000:00000:09990:99999")
bar07 = Image("00000:00000:00000:99999:99999")
bar08 = Image("00000:00000:00900:99999:99999")
bar09 = Image("00000:00000:09990:99999:99999")
bar10 = Image("00000:00000:99999:99999:99999")
bar11 = Image("00000:00900:99999:99999:99999")
bar12 = Image("00000:09990:99999:99999:99999")
bar13 = Image("00000:99999:99999:99999:99999")
bar14 = Image("00900:99999:99999:99999:99999")
bar15 = Image("09990:99999:99999:99999:99999")
bar16 = Image("99999:99999:99999:99999:99999")

barlist = [bar01, bar02, bar03, bar04, bar05, bar06, bar07, bar08, bar09, bar10, bar11, bar12, bar13, bar14, bar15, bar16]

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

    blist_Value = ((pwm * 16) // 1024)
    display.show(barlist[blist_Value])
