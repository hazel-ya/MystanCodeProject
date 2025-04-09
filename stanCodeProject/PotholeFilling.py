"""
File: PotholeFilling.py
Name: Hazel:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *
from StepUp import *


def put_99():
    for i in range(99):
        put_beeper()


def go_in():
    """
    pre-condition: Karel is at the upper left of the pothole facing East
    post-condition: Karel is in the pothole,facing South
    """
    move()
    turn_right()
    move()


def main():
    for i in range(3):
        go_in()
        put_99()
        go_out()


def go_out():
    """
    pre-condition: Karel is in the pothole,facing South
    post-condition: Karel is at the upper left of the pothole facing East
    """
    for i in range(2):
        turn_left()
    move()
    turn_right()
    move()




# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
