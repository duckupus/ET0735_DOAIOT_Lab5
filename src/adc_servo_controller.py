from threading import Thread
from time import sleep

from hal import hal_servo as hal_servo
from hal import hal_adc as hal_adc

def loop():
    while True:
        adc_val = hal_adc.get_adc_value(1)
        #print(adc_val)
        convert = 180 - (adc_val/6 % 181)
        hal_servo.set_servo_position(convert)


def main():
    hal_adc.init()
    hal_servo.init()
    loopthread = Thread(target=loop)
    loopthread.start()
    return

if __name__ == "__main__":
    main()