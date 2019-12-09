import sys
from datetime import datetime
import argparse
import random


class Parser():
    __parser = None
    __args = None

    def __init__(self, sysargs):
        self.__parser = self.__create_parser()
        self.__args = vars(self.__parser.parse_args(sysargs))
        print(f"Arg comand line in class: {self.__args}")

    def __create_parser(self):
        parser = argparse.ArgumentParser(description="main.py -digits [--fullmatch_sign --match_sign")
        parser.add_argument("-digits", type=int, default=4, help="")
        parser.add_argument("--fullmatch_sign", type=str, default="B", help="")
        parser.add_argument("--match_sign", type=str, default="K", help="")

        return parser

    def show_args(self):
        print(self.__args)


def main():
    class_parser = Parser(sys.argv[1:])
    print(f"Arg out of class: {sys.argv}")
    print(f"Get arg: {class_parser.show_args()}")
    class_game1 = Game(3, "B", "K")
    class_game2 = Game(4, "B", "S")
    class_game1.show_parameters
    class_game2.show_parameters
    print(f"Number x3: {class_game1.game_count_triplet()}")
    # class_wordgame = WordGame()
    print(f"Public - digits_public: {class_game1.digits_public}")
    print(f"Random num: {class_game1.number}")

def count_triplet(self):
    return self.digits_public*3

class Gamer():
    __history = None
    __counter = 0

    def __init__(self):
        self.__counter = 0
        self.__history = dict()

    @property
    def next_move(self):
        user_number = self.user_number
        self.__counter += 1
        self.__history[self.__counter] = {"user_number": user_number,
                    "match_result":""}
        return user_number

    def set_result(self, result):
        self.__history[self.__counter]["match_result": result]

    @property
    def user_number(self):
        user_number =  input("Input number: ")
        if user_number.isdecimal():
            return user_number
        else:
            print("Not number")
            return "0000"

class Game():
    __fullmatch = ""
    __match = ""
    __digits = 4
    digits_public = 4
    __number = "0000"

    game_count_triplet = count_triplet

    def __rand_generator(self, digits):
        random.seed()
        s = ""
        for r in range(digits+1):
            s += str(random.randrange(10))
        return s

    def __init__(self, digits, fullmatch, match):
        self.__fullmatch = fullmatch
        self.__match = match
        self.__digits = digits
        self.digits_public = digits
        self.__number = self.__rand_generator(digits)
        # print(self.__number)

    @property
    def show_parameters(self):
        print(f"{self.__class__} Number of digits in number: {self.__digits}, full match mark: {self.__fullmatch},partial match mark: {self.__match}, generated number: {self.__number}")

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value


class Round():
    __game = None
    __gamer = None

    def __init__(self):
        self.__game = Game(4, "", "")
        self.__gamer = Gamer()
        self.worker()

    def __compare(self, number, user_number):
        if number == user_number:
            print("You guessed the number!")
            return True

        if len(number) != len(user_number):
            print("Different size numbers entered!")
            return False

        outB = str()
        outK = str()

        for i in range(len(number)):
	        for j in range(len(user_number)):
		        if number[i] == user_number[j]:
			        if i == j:
				        outB += "B"
			        else:
				        outK += "K"

        print(outB + outK)
        return False

    def worker(self):
        n1 = self.__game.number
        while True:
            n2 = self.__gamer.next_move
            won = self.__compare(n1, n2)
            if won:
                print("You won!")
                break


if __name__ == "__main__":
    main()