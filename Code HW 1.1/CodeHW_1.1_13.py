from microbit import *
import random

# Declare function for title 'screen' dialogue
def title_screen():
    while True:
        if (button_b.was_pressed()):
            game()
        elif (button_a.was_pressed()):
            instructions()
        display.scroll('Odd or Not * (A) FOR INSTRUCTIONS * (B) TO START * ')
        sleep(2000)

# Declare function for displaying instructions
def instructions():

    # instructions message
    display.scroll('Press ')
    display.show(Image.ARROW_W)
    sleep(500)
    display.scroll(' for ODD #s and ')
    display.show(Image.ARROW_E)
    sleep(500)
    display.scroll('for EVEN #S - fast!')
    sleep(1000)
    display.scroll('(A) TO REPEAT (B) TO START')
    sleep(2500)

    # view instructions or start game
    if (button_a.was_pressed()):
        instructions()
    elif (button_b.was_pressed()):
        game()

# Declare function for game loop
def game():

    # Assign variables for # of rounds/rounds won
    # Initial values 0 for counts (loop iterations and scoring)
    rounds = 0
    rounds_won = 0

    # Will run for 5 iterations
    while (rounds < 5):

        num = random.randint(1, 99)  # generates random number from 1-99
        num_mod = num % 2  # checks if num odd/even (divisible by 2 or not)

        display.scroll('.....')
        display.scroll(num)

        if (button_a.was_pressed()):  # button A for ODD
            if (num_mod == 1):  # num is ODD
                display.show(Image.YES)
                sleep(2000)
                rounds_won += 1
                rounds += 1
            elif (num_mod == 0):  # num is EVEN
                display.show(Image.NO)
                sleep(2000)
                rounds += 1

        elif(button_b.was_pressed()):  # button B for EVEN
            if (num_mod == 1):  # num is ODD
                display.show(Image.NO)
                sleep(2000)
                rounds += 1
            elif (num_mod == 0):  # num is EVEN
                display.show(Image.YES)
                sleep(2000)
                rounds_won += 1
                rounds += 1
        else:
            rounds += 1

    display.scroll('...!')
    sleep(1000)

    # Display score
    display.scroll('SCORE: ' + str(rounds_won) + '/' + str(rounds))
    sleep(3000)

    # Replay or exit to title screen
    while True:
        display.show(Image.ARROW_W)
        sleep(500)
        display.scroll('TO REPLAY')
        sleep(1000)
        display.show(Image.ARROW_E)
        sleep(500)
        display.scroll('TO EXIT')

        if (button_a.was_pressed()):
            game()
        elif (button_b.was_pressed()):
            break
        else:
            sleep(6000)

sleep(1000)

# Call title 'screen' function
title_screen()