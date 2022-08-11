import random

from ListGenerator import ListGenerator


class PasswordGenerator:
    """Generates a random password"""

    def __init__(self, adjectives="adjectives.txt", nouns="nouns.txt", punctuation="punctuation.txt"):
        self.__adjectives = ListGenerator(adjectives)
        self._random_adjective = random.choice(self.__adjectives.get_data())
        self.__nouns = ListGenerator(nouns)
        self._random_noun = random.choice(self.__nouns.get_data())
        self.__number = random.randint(0, 100)
        self.__punctuation = ListGenerator(punctuation)
        self.__random_punctuation = random.choice(self.__punctuation.get_data())

    def __str__(self) -> str:
        return self._random_adjective + self._random_noun + str(self.__number) + self.__random_punctuation
