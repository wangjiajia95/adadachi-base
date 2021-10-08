from constants import STATUS
from adadachi import Adadachi
import random


class Player:
    def __init__(self):
        self.adadachi = None
        self.inventory = {
            "games": ["hide-n-seek", "tag", "go fish", "red rover"],
            "foods": ["banana cream pie", "carrot sticks", "mashed potatoes", "mac 'n cheese", "tater tots", "chocolate cake", "strawberries", "fried rice"],
        }
        # self.hungry = Adadachi(self.name, self.personality)

    def play_with_adadachi(self):
        count = 0
        while count < 100:
            game = input(
                "which one you want to play? Options: 1.hide-n-seek, 2.tag, 3.go fish, 4.red rover, 5.stop")
            if game == "5":
                break
            if game == "1":
                print("Game started! let's hide-n-seek")
            if game == "2":
                print("Game started! let's tag")
            if game == "3":
                print("Game started! let's go fish")
            if game == "4":
                print("Game started! let's red rover")
            count += 1
        return count

    def get_status(self):
        play_times = self.play_with_adadachi()
        if play_times > 3:
            return True

    def feed(self):
        food = input("what do you want to eat? 1.banana cream pie , 2.carrot sticks, 3.mashed potatoes, 4.mac 'n cheese, 5.tater tots, 6.chocolate cake, 7.strawberries, 8.fried rice")
        return food

    def clean(self):
        return True

    def break_hachi(self):
        if self.clean():
            return True
        else:
            False
