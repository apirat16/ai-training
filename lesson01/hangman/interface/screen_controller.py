import subprocess as sp
from typing import List


class ScreenController(object):

    def __init__(self):
        ScreenController.clear_screen()

    @staticmethod
    def clear_screen():
        sp.call('clear', shell=True)

    @staticmethod
    def screen_output(question: str, hint: str, guess: List):
        print("PRESS ESC TO EXIT")
        print("")
        print("   +--------+")
        print("   |        |")
        print("   |        O")
        print("   | ")
        print("   | ")
        print("   | ")
        print("   | ")
        print("=======")
        print("")
        print("Question: {}".format(" ".join(list(question))))
        print("")
        print("Hint: {}".format(hint))
        print("")
        print("Guess: {}".format(" ".join(list(guess))) if guess is not None else "")
