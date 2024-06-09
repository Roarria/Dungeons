from time import time
from random import choice
from characters import Hero
from rooms import Treasure, Trap, Fight
from items import Item

class Game_Manager:
    def __init__(self, hero: Hero):
        self._start_time = None
        self.room_number = 0
        self.hero = hero

    def go_next(self):
        while True:
            start = input()
            if start == '':
                break
            else:
                print("To nie jest Enter :)")

    def start_clock(self):
        self._start_time = time()

    def summarize(self):
        print(f'PODSUMOWANIE:\n{self.hero}, {self.hero.get_class()}')
        print("Czas przejscia: ", time() - self._start_time)
        print(self.hero.get_stats())

    def create_map(self):
        room_pool = [Treasure(difficulty=1) for _ in range(4)] + [Fight(difficulty=1) for _ in range(5)] + [Trap(difficulty=1) for _ in range(3)]
        map = [choice(room_pool) for _ in range(9)]     # wybranie 9. pokoi
        map.append(Fight(difficulty=4))     # dodanie walki z bossem
        # zmiana poziomu trudnosci pokojow ?
        return map

    

hero = Hero(name = input("Podaj imie swojego bohatera: "))
hero.class_choice()
game_manager = Game_Manager(hero)
map = game_manager.create_map()

print(f'\n{hero}, zostales wrzucony do lochu. Przejdz przez 10 pokojow i pokonaj Straznika, aby sie wydostac. Gotowy? (wcisnij Enter)')
game_manager.go_next()  # usunac metode?
game_manager.start_clock()

while game_manager.room_number <= 9:
    print(f'============================== Pokoj {game_manager.room_number + 1} ==============================')
    result = map[game_manager.room_number].enter(hero)

    if result == 'game_over':
        print('Nie udalo ci sie opuscic lochu zywym.')
        break
    if isinstance(result, Item):      # zebranie skarbu/nagrody po walce
        hero.equip_item(result)
    
    print()
    print(hero.get_stats())
    print(hero.show_items())
    game_manager.room_number += 1

    if hero.items:
        choice = input('Czy chcesz uzyc jakiegos przedmiotu? (tak, nie) ').casefold()
        while True:
            if choice == 'tak':
                item_str = input(f'Wybierz przedmiot: ').casefold()
                while True: 
                    item = None                       
                    for i in hero.items:
                        if i.get_name() == item_str:
                            item = i
                    if item:
                        hero.use_item(item)
                        print(f'Uzyto {item_str}.\n')
                        print(hero.get_stats())
                        print(f'{hero.show_items()}\n')
                        break
                    else:
                        item = input('Nie rozpoznano wyboru. Sprobuj ponownie: ').casefold()
                break
            elif choice == 'nie':
                break
            else:
                choice = input('Nie rozpoznano wyboru. Sprobuj ponownie: ')

    input('Zbierz sily i przejdz dalej.\n')

print("Koniec gry\n")
game_manager.summarize()

