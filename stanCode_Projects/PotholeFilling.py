"""
File: PotholeFilling.py
Name: willy
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    """
    willy's python lesson
    """
    for i in range(2):
        for i in range(3):
            go_in1()
            put_99()
            go_out1()
        turn_around()
        for i in range(3):
            go_in2()
            pick_99()
            go_out2()
        turn_around()


def go_in1():
    """
    pre-condition:Karel is at the upper left of the pothole,facing East.
    post-condition:Karel is in the pothole.facing South.
    """
    move()
    turn_right()
    move()


def go_in2():
    """
    """
    move()
    turn_left()
    move()


def go_out1():
    """
    pre-condition:Karel is in the pothole.facing South.
    post-condition:Karel is in the pothole.facing South.
    """
    turn_around()
    move()
    turn_right()
    move()


def go_out2():
    """

    """
    turn_around()
    move()
    turn_left()
    move()


def turn_right():
    for i in range(3):
        turn_left()


def put_99():
    """Karel will put 99 beepers"""
    for i in range(99):
        put_beeper()


def pick_99():
    """Karel will pick 99 beepers"""
    for i in range(99):
        pick_beeper()


def turn_around():
    for i in range(2):
        turn_left()






# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
