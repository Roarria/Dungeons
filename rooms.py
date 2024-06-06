from abc import ABC, abstractmethod
from characters import Enemy
from items import Item

class Room(ABC):
    @abstractmethod
    def enter(self):
        pass

class Treasure(Room):
    def enter(self):
        print("treasure")

class Fight(Room):    # 3-5 i boss
    def enter(self):
        print("fight")

class Trap(Room):
    def enter(self):
        print("trap")