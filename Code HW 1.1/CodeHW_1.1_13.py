from microbit import *
import random

# 'pause' function via stackexchange
# def hold():
#    hold = input("Press the <ENTER> key to continue...")


# Function called to start the game
def game():
    rounds = 0
    rounds_won = 0

    while (rounds < 3):

        num = random.randint(1, 9)
        num_mod = num % 2

        display.scroll('.....')
        display.scroll(num)

        if (button_a.was_pressed()):
            if (num_mod == 1):
                display.show(Image.YES)
                sleep(2000)
                rounds_won += 1
                rounds += 1
            elif (num_mod == 0):
                display.show(Image.NO)
                sleep(2000)
                rounds += 1

        elif(button_b.was_pressed()):
            if (num_mod == 1):
                display.show(Image.NO)
                sleep(2000)
                rounds += 1
            elif (num_mod == 0):
                display.show(Image.YES)
                sleep(2000)
                rounds_won += 1
                rounds += 1
        else:
            rounds += 1

    display.scroll('....!')
    sleep(1000)
    display.scroll('Score: ' + str(rounds_won) + '/' + str(rounds))
    sleep(3000)
    display.scroll('Shake to play again!')
    if (accelerometer.was_gesture('shake')):
        game()
    else:
        sleep(6000)

def instructions():
    display.scroll('PRESS (A) IF THE # IS ODD AND (B) IF IT IS EVEN.')
    sleep(1000)
    display.scroll('(A) TO START (B) TO REPEAT')
    if (button_a.was_pressed()):
        game()
    elif (button_b.was_pressed()):
        instructions()

while True:
    display.scroll('T')  # ODD OR NOT * (A) TO START * (B) FOR INSTRUCTIONS
    if (button_a.was_pressed()):
        game()
    elif (button_b.was_pressed()):
        instructions()
    sleep(2000)