from action import *

PISTOL_PICKED = False
NUMBER_OF_BULLETS = random.randint(1, 5)
KEY_PICKED = False
FOOD_PICKED = False
GRENADE_PICKED = False
BASEMENT = False
LIFE_POINTS = 20


def room(argument):
    switcher = {
        2: room2,
        3: room3,
        4: room4,
        5: room5,
        6: room6,
        7: room7,
        8: room8,
        9: room9,
        10: room10,
        11: room11,
        12: room12,
        13: room13,
        14: room14,
        15: room15,
        16: room16,
        17: room17,
        18: room18,
        19: room19,
        20: room20
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "Invalid month")
    # Execute the function
    print
    func()


def room2():
    response = input("You find some ghosts who are attacking you! What do you do: run away or fight?\n")
    response = validate_user_input(response, "fight", "run away")
    global LIFE_POINTS
    if response == "fight":
        LIFE_POINTS = fight_ghosts()
    elif response == "run away":
        run_away()


def room3():
    response = input("You see a pistol on the table: pick or leave?")
    response = validate_user_input(response, "pick", "leave")
    if response == "pick":
        global PISTOL_PICKED
        pick_pistol()
        PISTOL_PICKED = True
    elif response == "leave":
        pass


def room4():
    response = input("There is a key near the window: pick or leave?")
    response = validate_user_input(response, "pick", "leave")
    if response == "pick":
        pick_key()
        global KEY_PICKED
        KEY_PICKED = True
    elif response == "leave":
        pass


def room5():
    global NUMBER_OF_BULLETS
    response = input("There is a monster in deep sleep, will you shoot or run?")
    response = validate_user_input(response, "shoot", "run")
    if response == "shoot":
        if PISTOL_PICKED:
            fire_pistol()
            NUMBER_OF_BULLETS = NUMBER_OF_BULLETS - 1;
        else:
            print("Oops You did not pick the pistol!, You will have to run")
    elif response == "run":
        pass


def room6():
    response = input("In this room you see a grenade with a pin, pick or leave?")
    response = validate_user_input(response, "pick", "leave")
    if response == "pick":
        pick_grenade()
        global GRENADE_PICKED
        GRENADE_PICKED = True
    elif response == "leave":
        pass


def room7():
    response = input("Finally you  have  found an elevator and stairs to the basement , elevator or stairs?")
    response = validate_user_input(response, "elevator", "stairs")
    if response == "elevator":
        take_elevator()

    elif response == "stairs":
        take_stairs()
        global BASEMENT
        BASEMENT = True


def room8():
    if BASEMENT:
        print("You are at the basement you can only go back up")
    else:
        global FOOD_PICKED
        global LIFE_POINTS
        response = input("Wo! You got food on a table before you, pick or leave?")
        response = validate_user_input(response, "pick", "leave")
        if response == "pick":
            food_points = pick_food()
            LIFE_POINTS += food_points
            print("Life points have been added to ", LIFE_POINTS)
            FOOD_PICKED = True
        elif response == "leave":
            LIFE_POINTS -= 1
            print("Life points have been reduced to ", LIFE_POINTS)


def room9():
    response = input("Here there is silence and the room is clean, you can choose to eat here or keep going , "
                     "eat or go?")
    response = validate_user_input(response, "eat", "go")
    global FOOD_PICKED
    global LIFE_POINTS
    if response == "eat":
        if FOOD_PICKED:
            eat_food()

            FOOD_PICKED = False
        else:
            LIFE_POINTS -= 1
            print("oops you did not pick any food")

    elif response == "go":
        pass


def room10():
    print("This room is very quiet there no sign of life here.")


def room11():
    print("You start to hear voices from a distance, be alert!")


def room12():
    print("There are audible sounds of what is people's voices in the next room, tread carefully!")


def room13():
    response = input("Boom! there are two armed men, they notice you, you will have to engage and run, either shoot "
                     "or throw grenade, "
                     " shoot or grenade?")
    response = validate_user_input(response, "shoot", "grenade")
    global GRENADE_PICKED
    global LIFE_POINTS
    if response == "shoot":
        if PISTOL_PICKED and NUMBER_OF_BULLETS > 0:
            fired = fire_pistol()
            LIFE_POINTS -= fired
        else:
            print("Oops You did not pick the pistol or ran out of bullets!, You will have to run ")
    elif response == "grenade":
        if GRENADE_PICKED:
            throw_grenade()
            seconds = random.randint(1, 5)
            print("grenade will go off in ", seconds, "seconds")
            for i in range(seconds):
                print("Second ", seconds - i)
                LIFE_POINTS -= 1
            print("Grenade went off but you are lucky to still be alive")
            print("Life points have been reduced to ", LIFE_POINTS)
            GRENADE_PICKED = False
        else:
            print("Oops You don't have a grenade!, You will have to run")


def room14():
    print("You hear steps following you, you have to move faster!")


def room15():
    print("You are doing good but you have to move faster")


def room16():
    global LIFE_POINTS
    print("Life points have been reduced to ", LIFE_POINTS - 1)
    if FOOD_PICKED:
        print(" You have to drop the food you are carrying, it is slowing you down")
    else:
        print("keep running")


def room17():
    global LIFE_POINTS
    print("Life points have been reduced to ", LIFE_POINTS - 1)
    print("keep moving")


def room18():
    global GRENADE_PICKED
    global LIFE_POINTS
    response = input(
        "As you want to leave from this room someone is banging the  door behind you, either shoot or throw grenade,"
        " shoot or grenade?")
    response = validate_user_input(response, "shoot", "grenade")
    if response == "shoot":
        if PISTOL_PICKED:
            fired = fire_pistol()
            LIFE_POINTS -= fired
        else:
            print("Oops You did not pick the pistol!, You will have to run ")
    elif response == "grenade":
        if GRENADE_PICKED:
            throw_grenade()
            time_seconds = random.randint(1, 5)
            print("grenade will go off in ", time_seconds, "seconds")
            for i in range(time_seconds):
                print("Second ", time_seconds - i)
                LIFE_POINTS -= 1
            print("Grenade went off but you are lucky to still be alive")
            print("Life points have been reduced to ", LIFE_POINTS)
            GRENADE_PICKED = False
            GRENADE_PICKED = False
        else:
            print("Oops You don't have a grenade!, You will have to run")


def room19():
    global LIFE_POINTS
    print("Life points have been reduced to ", LIFE_POINTS - 1)
    print("You have one more room to finally be out and safe")


def room20():
    global LIFE_POINTS
    print("You are in the last room now")
    print("Your Life points remaining are:", LIFE_POINTS)


def validate_user_input(response, v_one, v_two):
    while True:
        if response == v_one or response == v_two:
            break
        else:
            print("Enter a valid option!")
            response = input(
                "Please enter " + v_one + " or " + v_two + "\n")
    return response
