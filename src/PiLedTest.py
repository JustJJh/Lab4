import time
from hal import hal_input_switch as switch
from hal import hal_led as led

def blink_led(delay):
    # Led Blink
    led.init()

    led.set_output(0, 1)
    time.sleep(delay)

    led.set_output(0, 0)
    time.sleep(delay)

    led.set_output(0, 1)
    time.sleep(delay)

    led.set_output(0, 0)
    time.sleep(delay)
    
    
def main():
    switch.init()
   
    while(1):
        if switch.hal_input_switch():
            blink_led(0.2)
        else 
            blink_led(0.2)


if __name__ == "__main__":
    main()