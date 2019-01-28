import random
from typing import List


class GameEngine(object):

    _guess: List[str]

    def __init__(self):
        self._question = random.choice(self._get_question())
        self._guess = list()

    def get_guess(self):
        return self._guess

    @staticmethod
    def _get_question() -> List:
        """

        :return: list of questions and hint
        """
        questions = [
            {"question": "micheal jordan", "hint": "He's the basketball player."},
            {"question": "angelina jolie", "hint": "She's beautiful and has many children."},
            {"question": "donald trump", "hint": "He's rich."},
            {"question": "britney spears", "hint": "She's blond."},
        ]
        return questions

    def get_output(self):
        output = str(self._question["question"])
        for char in self._guess:
            if char.lower() in self._question["question"]:
                output = output.replace(char.lower(), char.upper())
        for char in output:
            if char.islower():
                output = output.replace(str(char), "_")
        return output

    def get_hint(self):
        return self._question["hint"] if "hint" in self._question else None

    def guess_character(self, char: chr) -> bool:
        """
        Guess the character in the word

        :return: True when the game is finished, otherwise False
        """
        if char[:1] not in self._guess:
            self._guess.append(char[:1].lower())

        return "_" not in self.get_output()
