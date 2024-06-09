from abc import abstractmethod
from items import Item
from random import choice, randint, choices

class Character:
    def __init__(self, name: str):
        self.name = name
        self.life = 100
        self.strength = (10, 20)
        self.shield = (10, 20)

    def __str__(self):
        return self.name
    
    def attack(self):
        return randint(self.strength[0], self.strength[1])
    
    def defence(self):
        return randint(self.shield[0], self.shield[1])
    
    @abstractmethod
    def choice(self):
        pass

    @abstractmethod
    def get_stats(self):
        pass



class Hero(Character):
    def __init__(self, name: str):
        super().__init__(name)
        self.hero_class = None
        self.items = []
        self.escape_chance = 50
        self.disarm_chance = 50

    def class_choice(self):
        print("\nDostepne klasy: wojownik, wlamywacz, zdrajca.\nWojownik: ma wieksza sile w walce.\nWlamywacz: lepiej rozbraja pulapki.\nZdrajca: ucieczka z pola walki czesciej konczy sie sukcesem.\n")
        while True:
            choice = input("Wybierz klase: ").casefold()
            if choice == "wojownik":
                self.strength = (18, 28)
                self.hero_class  = choice
                break

            elif choice == "wlamywacz":
                self.disarm_chance += 25
                self.hero_class = choice
                break

            elif choice == "zdrajca":
                self.escape_chance += 25
                self.hero_class = choice
                break

            else:
                print("Nie ma takiej klasy. Sprobuj ponownie: ")
    
    def choice(self):   # zmiana nazwy?
        while True:
            hero_move = input('Wybierz swoj ruch (atak, obrona, ucieczka): ').casefold()
            if hero_move in ['atak', 'obrona', 'ucieczka']:
                return hero_move
            else:
                print('Nie ma takiego wyboru. Wpisz ponownie.')

    def escape_try(self):
        success = choices((True, False), weights=(self.escape_chance, 100-self.escape_chance), k=1)[0]
        if success:
            print("Udalo ci sie uciec.")
        else:
            print("Nie udalo ci sie uciec.")
        return success
    
    def get_class(self):
        return self.hero_class
    
    def get_stats(self):
        return f'Statystyki bohatera: zycie - {self.life}, sila - {self.strength}, obrona - {self.shield}, szansa ucieczki - {self.escape_chance}, szansa rozbrojenia pulapki - {self.disarm_chance}'
    
    def show_items(self):
        str = 'Lista przedmiotow: '
        for item in self.items:
            str += f'{item.__str__()} '
        return str

    def equip_item(self, item):
        self.items.append(item)

    def use_item(self, item):
        for stat, value in item.stats.items():
            try:
                if isinstance(getattr(self, stat), int):
                    setattr(self, stat, min(100, getattr(self, stat) + value))

                elif isinstance(getattr(self, stat), tuple):
                    x, y = getattr(self, stat)
                    x += value
                    y += value
                    setattr(self, stat, (x, y))

            except Exception as e:
                print(e)
        
        self.items.remove(item)



class Enemy(Character):
    def __init__(self, name: str, life: int, strength: tuple, shield: tuple):
        self.name = name
        self.life = life
        self.strength = strength
        self.shield = shield

    def change_life(self, life):
        self.life = life
    
    def change_strength(self, strength):
        self.strength = strength
        
    def change_shield(self, shield):
        self.shield = shield

    def choice(self):
        return choice(['atak', 'obrona'])

    def defence(self):
        return randint(self.shield[0], self.shield[1])

    def get_stats(self):
        return f'Statystyki przeciwnika: zycie - {self.life}, sila - {self.strength}, obrona - {self.shield}'
