from random import randint
from playwriter import *


class Critic:
    __influence: int

    def __init__(self):
        self.__influence = 5

    @property
    def influence(self):
        return self.__influence

    @influence.setter
    def influence(self, influence: int):
        self.__influence = influence

    def criticize(self, playwriter: PlayWriter):
        score = randint(0, 10)
        print("score from Expert: ", score)
        if score <= 5:
            if self.influence >= playwriter.influence:
                playwriter.drink()
            else:
                self.__influence -= 1
        else:
            if self.influence >= playwriter.influence:
                playwriter.influence += 1
            else:
                self.__influence += 1
