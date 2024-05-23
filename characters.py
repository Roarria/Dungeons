class Character:
    def __init__(self, name = None):
        self.name = name
        self.life = 100
        self.strength = (10, 20)


class Hero(Character):
    def __init__(self, name = None):
        super().__init__(name)
        self.hero_class = None
        self.items = []
        self.escape_chances = 50
        self.disarm_chance = 50
    
    def rename(self):
        self.name = input("Podaj imie: ")

    def class_choice(self):
        print("Dostepne klasy: wojownik, wlamywacz, zdrajca.")
        print() # co robi kazda z klas
        while True:
            choice = input("Wybierz klase: ").casefold()
            if choice == "wojownik":
                self.strength = (18, 28)
                break

            elif choice == "wlamywacz":
                self.disarm_chance += 25
                break

            elif choice == "zdrajca":
                self.escape_chances += 25
                break

            else:
                print("Nie ma takiej klasy. Sprobuj ponownie: ")


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

