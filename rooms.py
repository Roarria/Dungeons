from abc import ABC, abstractmethod
from random import sample, choice, choices
from characters import Enemy, Hero
from items import Item


class Room(ABC):
    def __init__(self, difficulty):
        self.difficulty = difficulty

    @abstractmethod
    def enter(self, hero: Hero):
        pass

class Treasure(Room):
    treasures_pool = {1: [Item('jablko', {'life': 5}), Item('ser', {'life': 10})], 2: [], 3:[]}   # lista skarbow: 6 skarbow na poziom?

    def enter(self, hero: Hero):
        input("Otwierasz pokoj. Na srodku stoi skrzynia. Nie mozesz jej nie otworzyc. (wcisnij Enter)")
        treasures = sample(self.treasures_pool[self.difficulty], k=2)
        treas_names  = []
        for treasure in treasures:
            print(treasure)
            treas_names.append(treasure.get_name())

        while True:
            choice = input('Ktory skarb wybierasz? ')
            if choice in treas_names:
                return choice
            else:
                print('Nie ma takiego skarbu. Sprobuj wybrac ponownie.')


class Fight(Room):    # 3-5 i boss
    def __init__(self, difficulty):
        super().__init__(difficulty)
        # tworzenie statystyk przeciwnikow: ...
        self.enemies = {1: [Enemy('przeciwnik'), Enemy('kot')], 2: [], 3: []}

    def enter(self, hero: Hero):
        enemy = choice(self.enemies[self.difficulty])
        input(f"Otwierasz niepewnie drzwi. Na twojej drodze staje {enemy}. Szykuj sie do walki. (wcisnij Enter)")

        while enemy.life > 0:
            enemy.life = 0
            pass

"""  name, life, strength, shield
wyswietl statystyki przeciwnika
wyswietl planowany ruch (medota odpowiadajaca za ruch: atak, obrona)
decyduj (atak, obrona, uzycie przedmiotu, ucieczka)
[petla]
"""


class Trap(Room):
    def enter(self, hero: Hero):
        input("Pokoj wyglada na pusty. Przechodzisz przez niego spokojnie. Slyszysz dziwny zgrzyt pod swoja noga. To pulapka. Probujesz ja rozbroic. (wcisnij Enter)")
        success = choices((True, False), weights=(hero.disarm_chance, 100-hero.disarm_chance), k=1)[0]
        if success:
            print("Udalo ci sie rozbroic pulapke!")
        else:
            print("Tym razem ci sie nie udalo. Dostajesz 10 obrazen.")
            hero.life -= 10
