class Character:
    counter: int = 0

    def __init__(self, name: str, description: str):
        self.__name = name
        self.__description = description
        self.__id = Character.counter + 1
        Character.counter += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def id(self):
        return self.__id


class Event:
    counter: int = 0

    def __init__(self, name: str, description: str):
        self.__name = name
        self.__description = description
        self.__id = Event.counter + 1
        Event.counter += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def id(self):
        return self.__id
