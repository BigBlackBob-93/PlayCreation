from play import *
from critic import *


class PlayWriter:
    plays: list[Play] = []

    def __init__(self, nickname: str):
        self.__nickname = nickname
        self.__condition = 'alive'
        self.__mind = 100
        self.influence = 0

    @property
    def nickname(self):
        return self.__nickname

    @nickname.setter
    def nickname(self, nickname: str):
        self.__nickname = nickname

    @property
    def mind(self):
        return self.__mind

    @mind.setter
    def mind(self, mind: str):
        self.__mind = mind

    def add_play(self, title: str):
        play = Play(title)
        self.plays.append(play)

    def search_play(self, title: str):
        for i in self.plays:
            if i.title == title:
                return i
        return False

    def write(self, title: str, character_name: str, event_name: str):
        play = self.search_play(title)
        if not play:
            self.add_play(title)
            play = self.search_play(title)
        play.add_to_plot(character_name, event_name)

    def show(self):
        print("\nPLAYS:", end=" ")
        for i in self.plays:
            print(i.title, end=" ")

    def publish(self, title: str):
        flag: bool = False
        play = self.search_play(title)
        if play:
            play.show()
            print("--", self.nickname)
            critic = Critic()
            critic.criticize(self)
        else:
            print("You haven't written this yet")

    def drink(self):
        self.__mind -= 10
        if self.__mind < 1:
            self.__condition = 'dead'


if __name__ == '__main__':
    tom = PlayWriter("Tom")
    tom.write("story", "Mila", "death")
    tom.publish("story")
