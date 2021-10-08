from player import Player
from adadachi import Adadachi
from constants import *
import random

player = Player()


def display(statement):
    print(statement)


def create_adadachi():
    name = input(GET_NAME + "\n\t")
    foods = player.inventory["foods"]
    games = player.inventory["games"]
    personality = {
        # "fav_food": random.randint(0,len(foods)),
        "fav_food": "5",
        "fav_game": random.randint(0, len(games)),
        "hates_food": random.randint(0, len(foods)),
        "hates_game": random.randint(0, len(games)),
    }
    player.adadachi = Adadachi(name, personality)


def start_game():
    display(TITLE)
    answer = input(GREETING)
    if answer.lower() == "y":
        create_adadachi()
        while player.adadachi.hunger < 5:
            option = input(OPTIONS).lower()

            if option == "s":
                if player.get_status():
                    display(WON)
                else:
                    print("Can we play one more time?")

            elif option == "c":
                player.clean()
                if player.clean():
                    print("I dont like shower")
            elif option == "f":
                if player.inventory["foods"]:
                    if player.feed() == player.adadachi.personality["fav_food"]:
                        display(WON)
                else:
                    break
            elif option == "p":
                player.play_with_adadachi()
            elif player.break_hachi():
                display(LOST)

            elif option == "x":
                return display(EXIT)

        # display(LOST)
