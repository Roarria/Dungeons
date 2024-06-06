from time import time
from random import choice
import characters
import rooms

class Game_Manager:
    def __init__(self):
        self._start_time = None
        self.room_number = 0

    def start_clock(self):
        self._start_time = time()

    def summarize(self):
        print("Czas przejscia: ", time() - self._start_time)
        # ... statystyki

    def create_map(self):
        room_pool = [rooms.Treasure() for _ in range(4)] + [rooms.Fight() for _ in range(5)] + [rooms.Trap() for _ in range(3)]
        map = [choice(room_pool) for _ in range(9)]     # wybrane 9 pokoi (10 bedzie boss)
        for room, nr in enumerate(map):    # nr = 0, 1, ...
            pass
        return map

# (słownik z kluczami: 1-3, 4-6, 7-9) 
#losowanie: 9 z gornych granic + boss

game_manager = Game_Manager()
map = game_manager.create_map()

hero = characters.Hero(name = input("Podaj imie swojego bohatera: "))
hero.class_choice()

print(f'{hero}, zostales wrzucony do lochu. Przejdz przez 10 pokojow i pokonaj Straznika, aby sie wydostac. Gotowy? (wcisnij Enter)')
while True:
    start = input()
    if start == '':
        break
game_manager.start_clock()

while game_manager.room_number <= 8:
    print(game_manager.room_number, map[game_manager.room_number])
    map[game_manager.room_number].enter()
    game_manager.room_number += 1

print("Koniec gry")
game_manager.summarize()

