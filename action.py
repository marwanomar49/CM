import random

USER_LIFE_POINTS = 20


def fight_ghosts():
    global USER_LIFE_POINTS
    print("The ghosts are attacking us!!!!")
    number_of_ghosts = random.randint(1, 5)
    for i in range(number_of_ghosts):
        print("Ghost number ", i, " attacked us!")
        USER_LIFE_POINTS -= 1
    print("Life points have been reduced to ", USER_LIFE_POINTS)
    response = input("We see a chest in th corner! Should we open it (yes or no)?\n")
    if response == "yes":
        pass
    elif response == "no":
        pass
    return USER_LIFE_POINTS


def pick_key():
    print("Key Picked\n")
    # pick key


def pick_grenade():
    print("grenade picked!\n")


def throw_grenade():
    print("grenade throwm!\n")


def pick_pistol():
    print("pistol picked\n")


def pick_food():
    food = random.randint(1, 3)
    for i in range(food):
        print("Bullet", i, "fired!")
    return food
    print("Food picked\n")


def eat_food():
    print("Eating food!\n")


def open_door():
    print("Door Opened\n")


def fire_pistol():
    fired = random.randint(1, 5)
    for i in range(fired):
        print("Bullet", i, "fired!")
    return fired


def take_elevator():
    print("Taking elevator")


def take_stairs():
    print("Taking the stairs")


def run_away():
    print("Running away!")
