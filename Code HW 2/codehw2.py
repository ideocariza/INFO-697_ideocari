from microbit import *

# ##################################################
# ############### PROOF OF CONCEPT #################
# ##################################################

# Here, button_b stands in for the force sensitive
# resistor and an LED stands in for the full
# undeveloped circuit. This will show that:
#
# 1. While button_b (or force sensitive resistor -
#    FSR) is depressed AND a specified temperature is
#    not exceeded (here, 31º C), the circuit is closed
#    and the LED light (or heating current) on.
#
# 2. While the circuit is closed, if the temperature
#    does go above range, the current will
#    automatically shut off.
#
# 3. Items 1 and 2 are looped, switching the
#    circuit from open to closed as needed according
#    to continuous temperature readings. If the
#    temperature reading already exceeds the
#    prescribed range while button_b is pressed,
#    this loop will not begin.
#
# 4. While button_b (or force sensitive resistor -
#    FSR) is not depressed, the circuit remains closed.
#
#
# TO TEST THE CODE
#
# The temperature of 31º C was chosen to easily
# test the code based on the room temperature of my
# apartment. To test the code easily in other
# environments, this may need to be adjusted.
#
# Pressing and holding down Button B on the
# micro:bit while applying heat to the temperature
# sensor on the opposite side of the micro:bit with
# your fingers should increase the temperature
# a few degrees (to test the temp_regulate
# function).
#
# For the purposes of testing, current
# temperature readings are scrolled while button_b
# is pressed, and 'Hot!' followed by a temperature
# reading indicates that the prescribed temperature
# range has been exceeded. This is to provide
# feedback while testing.

# In-line comments indicate pseudo/remaining work,
# with remaining work labelled "CODE:".


while True:

    temp = temperature()  # define variable for temperature

    # CODE: define variable for default max temp
    # max_temp-d = 31

    # CODE: define variable for current max temp
    # max_temp-c = max_temp-d

    # CODE: define function for settings (so users can define new max temp)
    # def temp_settings
    #   max_temp-u = max_temp-c
    #   if button_a.was_pressed():
    #       display.scroll('Max. temp ')
    #       display.scroll(max_temp-c)
    #       sleep(1000)
    #       display.scroll('Press ')
    #       display.show(Image.ARROW_W)
    #       display.scroll(' to change or ')
    #       display.show(Image.ARROW_E)
    #       display.scroll(' to exit.')
    #       sleep(1000)
    #       if button_a.was_pressed():
    #           display.show(Image.ARROW_W)
    #           display.scroll(' to lower or ')
    #           display.show(Image.ARROW_E)
    #           display.scroll(' to increase. A+B to set.')
    #           if button_a.was_pressed():
    #               max_temp-u = (max_temp-c - 1)
    #               display.scroll(max_temp-u)
    #           elif button_b.was_pressed():
    #               max_temp-u = (max_temp-c + 1)
    #               display.scroll(max_temp-u)
    #           elif button_a.was_pressed and button_b.was_pressed():
    #               display.scroll('Set new? ')
    #               display.show(Image.ARROW_W)
    #               display.scroll(' to set, ')
    #               display.show(Image.ARROW_E)
    #               display.scroll(' to exit')
    #               sleep(1000)
    #               if button_a.was_pressed():
    #                   # CODE: update max_temp-c to equal max_temp-u
    #                   #       NOTE: nesting issues here
    #                   # CODE: display check mark
    #                   # CODE: exit settings
    #               elif button_b.was_pressed():
    #                   # CODE: exit settings
    #               else:
    #                   display.scroll(max_temp-c)

    if button_b.is_pressed():  # CODE: if FSR input...
        if(temp <= 31):  # CODE: if temp <= max_temp-c
            pin0.write_digital(1)
            display.scroll(temp)
            sleep(1000)
        else:
            display.scroll('Hot!')
            display.scroll(temp)
            pin0.write_digital(0)
    else:
        pin0.write_digital(0)
        display.show(Image.ARROW_E)