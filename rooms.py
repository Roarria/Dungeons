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
        treasures_dict = {}
        treasures = sample(self.treasures_pool[self.difficulty], k=2)
        for treasure in treasures:
            print(treasure)
            treasures_dict[treasure.get_name()] = treasure

        while True:
            chosen_treas = input('Ktory skarb wybierasz? ').casefold()
            if chosen_treas in treasures_dict:
                return treasures_dict[chosen_treas]
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
            print(f'Status przeciwnika: {enemy.get_stats()}')
            enemy_move = enemy.choice()

            if  enemy_move == 'attack':
                attack = enemy.attack()
                defence = 0
                print(f'Planowany ruch przeciwnika: {enemy_move} - {attack}')
            elif enemy_move == 'defence':
                attack = 0
                defence = enemy.defence()
                print(f'Planowany ruch przeciwnika: {enemy_move} - {defence}')
            
            print(f'Status przeciwnika: {hero.get_stats()}')
            hero_move = hero.choice()
            if hero_move == 'atak':
                enemy.life -= max(hero.attack() - defence, 0)

            elif hero_move == 'obrona':
                attack -= hero.defence()

            elif hero_move == 'ucieczka':
                if hero.escape_try():
                    break
            
            hero.life -= attack
            if hero.life <= 0:
                return  'game over'
            print()


class Trap(Room):
    def enter(self, hero: Hero):
        input("Pokoj wyglada na pusty. Przechodzisz przez niego spokojnie. Slyszysz dziwny zgrzyt pod swoja noga. To pulapka. Probujesz ja rozbroic. (wcisnij Enter)")
        success = choices((True, False), weights=(hero.disarm_chance, 100-hero.disarm_chance), k=1)[0]
        if success:
            print("Udalo ci sie rozbroic pulapke!")
        else:
            print("Tym razem ci sie nie udalo. Dostajesz 10 obrazen.")
            hero.life -= 10
