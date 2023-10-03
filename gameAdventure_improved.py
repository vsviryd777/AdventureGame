# Svirydzenka, adventure Game, Project2
import time
import random


def print_pause(message):
    print(message)
    time.sleep(2)


"""ANSI color code functions"""
def prRed(text): print("\033[91m {}\033[00m" .format(text))
def prGreen(text): print("\033[92m {}\033[00m" .format(text))
def prYellow(text): print("\033[93m {}\033[00m" .format(text))


def color_prompt_pause(text, color_function):
    color_function(text)
    time.sleep(2)


#information about game for user
def introduction():
    print_pause("You are a treasure hunter.You are in-front of the castle.")
    print_pause("You need to find treasure.")
    print_pause("It can be dangerous!!!")
    print_pause("You have the choice to enter the garage or the castle.")


def choose_door(tools):
    door = input("Enter 1 to open the in-front door castle.\n"
                 "Enter 2 to open the garage door.\n"
                 "Please enter 1 or 2: ")
    if door == '1':
        random_scenary_castel(tools)
    elif door == '2':
        random_scenary_garage(tools)
    else:
        print_pause("Wrong,you need enter number 1 or 2.Try again.")
        choose_door(tools)


def castel_door1(tools):
    print_pause("You are entering into the castle.")
    print_pause("Here is the  hungry tiger.")
    if "food" in tools:
        print_pause("You give food to a hungry tiger, he falls asleep.")
        color_prompt_pause("Congratulation. You won. You got your treasure.", prGreen)
    else:
        color_prompt_pause("The tiger attacked you. You lose game. ", prRed)
    restart()


def castel_door2(tools):
    print_pause("You are entering into the castle.")
    print_pause("You see a big safe. You need key.")
    if "key" in tools:
        print_pause("You have key already. Open the safe.")
        color_prompt_pause("Congratulation. You won. You got your treasure.", prGreen)
        restart()
    else:
        print_pause("You can not open the safe.")
        print_pause("You need find a key.")
        print_pause("You can find it in garage.")
        choose_door(tools)


def castel_door3(tools):
    print_pause("You are entering into the castle.")
    print_pause("You see a Dragon. You need fight.")
    if "sword" in tools:
        print_pause("You have sword.Fight with Dragon .")
        print_pause("You have defeated the Dragon.")
        color_prompt_pause("Congratulation. You won. You got your treasure.", prGreen)
    else:
        color_prompt_pause("The Dragon defeated  you. You lose game. ", prRed)
    restart()


def garage_door1(tools):
    print_pause("You are entering into the garage.")
    if "food" in tools:
        print_pause("You already got food for hungry tiger.\n"
                    "It is nothing to do here.")
    else:
        print_pause("You found some food.\n"
                    "Take it. That will help you in your adventure.")
        tools.append("food")
    choose_door(tools)


def garage_door2(tools):
    print_pause("You are entering into the  garage.")
    if "key" in tools:
        print_pause("You already got key.\n"
                    "It is nothing to do here.")
    else:
        print_pause("You found a key.Keep it.")
        tools.append("key")
    choose_door(tools)


def garage_door3(tools):
    print_pause("You are entering into the garage.")
    if "sword" in tools:
        print_pause("You already got sword.\n"
                    "It is nothing to do here.")
    else:
        print_pause("You found a sword.Keep it.")
        tools.append("sword")
    choose_door(tools)


def random_scenary_castel(tools):
    random_number = random.randint(1, 3)
    if random_number == 1:
        castel_door1(tools)
    elif random_number == 2:
        castel_door2(tools)
    elif random_number == 3:
        castel_door3(tools)
    return


def random_scenary_garage(tools):
    mylist = random.randint(1, 3)
    if mylist == 1:
        garage_door1(tools)
    elif mylist == 2:
        garage_door2(tools)
    elif mylist == 3:
        garage_door3(tools)
    return

#play again
def restart():
    again = input("Would you like play again? Enter (y or n):  ").lower()
    if again == "n":
        color_prompt_pause('GAME OVER. Goodbye. See you next time.', prGreen)
    elif again == "y":
        color_prompt_pause('Great. Let`s play again!!!', prYellow)
        play_game()


def play_game():
    tools = []
    introduction()
    choose_door(tools)

if __name__ == "__main__":
    play_game()


