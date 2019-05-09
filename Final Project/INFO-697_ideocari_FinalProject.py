from microbit import *

pin8.write_digital(0)

while True:
    display.off()

    pressure = (pin0.read_analog())

    v = pin10.read_analog()
    mV = v * (5000 / 1024)
    c = .005 * (mV) + 4.4375

    if((pressure >= 1023) and (c <= 35)):
        pin8.write_digital(1)
    elif((pressure >= 1023) and (temp >= 36)):
        break
    else:
        pin8.write_digital(0)