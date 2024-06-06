from items import Item

class Character:
    def __init__(self, name = None):
        self.name = name
        self.life = 100
        self.strength = (10, 20)

    def __str__(self):
        return self.name


class Hero(Character):
    def __init__(self, name = None):
        super().__init__(name)
        self.hero_class = None
        self.items = []
        self.escape_chance = 50
        self.disarm_chance = 50

    def class_choice(self):
        print("\nDostepne klasy: wojownik, wlamywacz, zdrajca.\nWojownik: ma wieksza sile w walce.\nWlamywacz: lepiej rozbraja pulapki.\nZdrajca: ucieczka z pola walki czesciej konczy sie sukcesem.")
        while True:
            choice = input("Wybierz klase: ").casefold()
            if choice == "wojownik":
                self.strength = (18, 28)
                break

            elif choice == "wlamywacz":
                self.disarm_chance += 25
                break

            elif choice == "zdrajca":
                self.escape_chance += 25
                break

            else:
                print("Nie ma takiej klasy. Sprobuj ponownie: ")
    
    def equip_item(self, item):
        self.items.append(item)

    def use_item(self, item):
        for stat, value in item.stats.items():
            try:
                setattr(self, stat, getattr(self, stat) + value)
            except Exception as e:
                print(e)



class Enemy(Character):
    def __init__(self, name = None):
        super().__init__(name)
        self.shield = (10, 20)
    
    def change_life(self, life):
        self.life = life
    
    def change_strength(self, strength):
        self.strength = strength
        
    def change_shield(self, shield):
        self.shield = shield

