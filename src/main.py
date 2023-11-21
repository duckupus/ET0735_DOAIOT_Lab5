from time import sleep
from threading import Thread
from hal import hal_keypad as keypad
from hal import hal_lcd as LCD
from led_control import led_control_init

#Empty list to store sequence of keypad presses
password = []

lcd = LCD.lcd()
lcd.lcd_clear()

global LED_control_state
#Call back function invoked when any key on keypad is pressed
def key_pressed(key):
    password.append(key)
    global LED_control_state
    from led_control import set_control_state
    lcd.lcd_clear()
    lcd.lcd_display_string("LED Control", 1)
    if key == 0:
        LED_control_state = 0
        lcd.lcd_display_string("OFF LED", 2)
    elif key == 1:
        LED_control_state = 1
        lcd.lcd_display_string("Blink LED", 2)
    set_control_state(LED_control_state)

    print(password)


def main():
    # Initialize LCD
    lcd = LCD.lcd()
    lcd.lcd_clear()
    global LED_control_state
    LED_control_state = 0

    # Display something on LCD
    lcd.lcd_display_string("LED Control", 1)
    lcd.lcd_display_string("0:Off1:Blink", 2)
    sleep(1)

    # Initialize the HAL keypad driver
    keypad.init(key_pressed)

    # Start the keypad scanning which will run forever in an infinite while(True) loop in a new Thread "keypad_thread"
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()
    led_control_init()


# Main entry point
if __name__ == "__main__":
    main()
