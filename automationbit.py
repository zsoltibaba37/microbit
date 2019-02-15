#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from microbit import *


# ---------------------------------------------------------------------------------------------------------------------
def digital_in_1():
    """
    Automation:bit board Digital input 1
    :return: 0 or 1
    """
    input_1 = pin8.read_digital()
    return input_1


def digital_in_2():
    """
    Automation:bit board Digital input 2
    :return: 0 or 1
    """
    input_2 = pin13.read_digital()
    return input_2


def digital_output_1(do):
    """
    Automation:bit board Digital Output 1
    :param do: Int 0 or 1
    """
    pin14.write_digital(do)


def digital_output_2(do):
    """
    Automation:bit board Digital Output 2
    :param do: Int 0 or 1
    """
    pin15.write_digital(do)


def relay_output(op):
    """
    Automation:bit board Relay Output
    :param op: Int 0 or 1
    """
    pin16.write_digital(op)


def analog_input_1():
    """
    Automation:bit board Analog Input 1
    :return: 0 - 1023
    """
    analog_1 = pin2.read_analog()
    return analog_1


def analog_input_2():
    """
    Automation:bit board Analog Input 2
    :return: 0 - 1023
    """
    analog_2 = pin1.read_analog()
    return analog_2


def analog_input_3():
    """
    Automation:bit board Analog Input 3
    :return: 0 - 1023
    """
    analog_3 = pin0.read_analog()
    return analog_3


# ---------------------------------------------------------------------------------------------------------------------
t = 150         # delay
s = 500         # sleep time
bol = False     # monospace BOOL

while True:
    # DIGITAL In
    a = digital_in_1()
    display.scroll("di1:%d" % a, delay=t)
    sleep(s)

    b = digital_in_2()
    display.scroll("di2:%d" % b, delay=t)
    sleep(s)

    # DIGITAL Out
    digital_output_1(1)
    display.scroll("do1:ok", delay=t)
    sleep(s)
    digital_output_1(0)

    digital_output_2(1)
    display.scroll("do2:ok", delay=t)
    sleep(s)
    digital_output_2(0)


    if a == 1:
        relay_output(1)
        display.scroll("rel:on", delay=t)
        sleep(1000)
        relay_output(0)
        display.scroll("rel:off", delay=t)
        sleep(1000)

    # ANALOG In
    d = analog_input_1()
    display.scroll("an1:%d" % d, delay=t)
    sleep(s)

    e = analog_input_2()
    display.scroll("an2:%d" % e, delay=t)
    sleep(s)

    f = analog_input_3()
    display.scroll("an3:%d" % f, delay=t)
    sleep(s)

