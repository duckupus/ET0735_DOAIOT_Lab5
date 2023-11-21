from hal import hal_led as led
from threading import Thread
from time import sleep

from hal import hal_keypad as keypad

global LED_control_state


def set_control_state(x: int):
    global LED_control_state
    LED_control_state = x


def led_thread():
    global delay

    delay = 1
    while True:
        if LED_control_state == 0:
            led.set_output(20, 0)
            continue
        if delay != 0:
            led.set_output(20, 1)
            sleep(delay)
            led.set_output(20, 0)
            sleep(delay)


def led_control_init():
    global delay
    led.init()
    global LED_control_state
    LED_control_state = 0

    t1 = Thread(target=led_thread)

    t1.start()
    delay = 1
