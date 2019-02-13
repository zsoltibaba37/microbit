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
    analog_1 = pin2.read_digital()
    return analog_1


def analog_input_2():
    """
    Automation:bit board Analog Input 2
    :return: 0 - 1023
    """
    analog_2 = pin1.read_digital()
    return analog_2


def analog_input_3():
    """
    Automation:bit board Analog Input 3
    :return: 0 - 1023
    """
    analog_3 = pin0.read_digital()
    return analog_3


# ---------------------------------------------------------------------------------------------------------------------
while True:
    display.scroll("321", delay=100)

    # DIGITAL In
    a = digital_in_1()
    display.scroll("a %d" % a, delay=100)
    sleep(500)

    b = digital_in_2()
    display.scroll("b %d" % b, delay=100)
    sleep(500)

    c = a + b
    display.scroll("c %d" % c, delay=100)


    # DIGITAL Out
    digital_output_1(1)
    display.scroll("do1 ok", delay=100)
    sleep(500)

    digital_output_2(1)
    display.scroll("do2 ok", delay=100)
    sleep(500)

    relay_output(1)
    display.scroll("rel ok", delay=100)
    sleep(500)


    # ANALOG In
    d = analog_input_1()
    display.scroll("%d An1 ok"% d, delay=100)
    sleep(500)

    d = analog_input_2()
    display.scroll("%d An2 ok"% d, delay=100)
    sleep(500)

    d = analog_input_3()
    display.scroll("%d An3 ok"% d, delay=100)
    sleep(500)

