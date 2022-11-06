from play_elements import *


class Play:
    plot = {}
    characters: list[Character] = []
    events: list[Event] = []

    def __init__(self, title: str):
        self.__title = title

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    def show(self):
        print("\nCHARACTERS:", end=" ")
        for i in self.characters:
            print(i.name, end=" ")
        print("\nEVENTS:", end=" ")
        for i in self.events:
            print(i.name, end=" ")
        print("\nPLOT:", end=" ")
        print(self.plot.items())

    def add_character(self, name: str, description: str = "No description"):
        smth = Character(name, description)
        self.characters.append(smth)

    def add_event(self, name: str, description: str = "No description"):
        smth = Event(name, description)
        self.events.append(smth)

    def search_character(self, name: str):
        for i in self.characters:
            if i.name == name:
                return i
        return False

    def search_event(self, name: str):
        for i in self.events:
            if i.name == name:
                return i
        return False

    def del_character(self, name: str):
        smth = self.search_character(name)
        print("\nWow! It's better to kill him...")

    def del_event(self, name: str):
        smth = self.search_event(name)
        print("\nWhat happens in Play, stays in Play")

    def add_to_plot(self, character_name: str, event_name: str):
        character = self.search_character(character_name)
        event = self.search_event(event_name)

        if character and event:
            self.plot.update({character.name: event.name})
        else:
            if not character:
                self.add_character(character_name)
                character = self.search_character(character_name)
            if not event:
                self.add_event(event_name)
                event = self.search_event(event_name)
            self.plot.update({character.name: event.name})
