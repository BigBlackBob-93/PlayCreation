from play_elements import *


class Play:
    plot: list[int]
    characters: list[Character]
    events: list[Event]

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
            self.plot.insert(event.id, character.id)
        else:
            if not character:
                character = bool(input("\nThis character was not created. Create?"))
                if character:
                    self.add_character(character_name)
                else:
                    quit()
            if not event:
                event = bool(input("\nThis character was not created. Create?"))
                if event:
                    self.add_event(event_name)
                else:
                    quit()
            self.plot.insert(self.events[-1].id, self.characters[-1].id)
