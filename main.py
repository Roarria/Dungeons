from time import time
from random import choice
from characters import Hero
from rooms import Treasure, Trap, Fight

class Game_Manager:
    def __init__(self):
        self._start_time = None
        self.room_number = 0

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
        print("Czas przejscia: ", time() - self._start_time)
        # ... statystyki

    def create_map(self):
        room_pool = [Treasure(difficulty=1) for _ in range(4)] + [Fight(difficulty=1) for _ in range(5)] + [Trap(difficulty=1) for _ in range(50)]
        map = [choice(room_pool) for _ in range(9)]     # wybrane 9 pokoi (10 bedzie boss)
        for room, nr in enumerate(map):    # nr = 0, 1, ...
            pass
        return map

    

game_manager = Game_Manager()
map = game_manager.create_map()

hero = Hero(name = input("Podaj imie swojego bohatera: "))
hero.class_choice()

print(f'{hero}, zostales wrzucony do lochu. Przejdz przez 10 pokojow i pokonaj Straznika, aby sie wydostac. Gotowy? (wcisnij Enter)')
game_manager.go_next()
game_manager.start_clock()

while game_manager.room_number <= 8:
    choice = map[game_manager.room_number].enter(hero)

    if choice:      # zebranie skarbu/nagrody po walce
        hero.equip_item(choice)
        
    print(hero.get_stats(), hero.items)
    game_manager.room_number += 1
    print('Zbierz sily i przejdz dalej. (wcisnij Enter)')
    game_manager.go_next()

print("Koniec gry")
game_manager.summarize()

