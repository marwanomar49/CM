import random
from rooms import room

USER_LIFE_POINTS = 20
ROOM_NUMBER = 1


def enter_the_house():
    print("Welcome to the haunted house!")
    response = input("You see two doors, one to the left, and one to your right! Which one do you want to open?\n")
    while True:
        if response == "left" or response == "right":
            break
        else:
            print("Enter a valid room!")
            response = input(
                "You see two doors, one to the left, and one to your right! Which one do you want to open?\n")
    if response == "left":
        enter_left_room()
    if response == "right":
        enter_right_room()
    print("You have visited all the rooms! \n")


def enter_left_room():
    global ROOM_NUMBER
    ROOM_NUMBER = ROOM_NUMBER + 1
    if ROOM_NUMBER <= 20:
        current_room()


def enter_right_room():
    global ROOM_NUMBER
    ROOM_NUMBER = ROOM_NUMBER + 1
    if ROOM_NUMBER <= 20:
        current_room()


def current_room():
    print("You are in room:", ROOM_NUMBER, "\n")
    room(ROOM_NUMBER)
    response = input(
        "You see two doors, one to the left, and one to your right! Which one do you want to open?\n")
    response = validate_input(response)
    if response == "left":
        enter_left_room()
    if response == "right":
        enter_right_room()


def validate_input(response):
    while True:
        if response == "left" or response == "right":
            break
        else:
            print("Enter a valid room!")
            response = input(
                "You see two doors, one to the left, and one to your right! Which one do you want to open?")
    return response


def run():
    enter_the_house()
