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
    def __init__(self, difficulty):
        super().__init__(difficulty)
        ser = Item('ser', {'life': 5})
        jablko = Item('jablko', {'life': 10})
        bandaz = Item('bandaz', {'life': 15})
        penicylina = Item('penicylina', {'life': 20})

        rekawica = Item('rekawica', {'strength': 10})
        amulet = Item('amulet', {'strength': 15, 'life': -10})
        eliksir = Item('podejrzana fiolka', {'strength': 20, 'life': -20})

        helm = Item('stary helm', {'shield': 10})
        zbroja = Item('zardzewiala zbroja', {'shield': 15, 'life': -10})
        deska = Item('porzadna deska', {'shield': 15, 'strength': -10})

        zaslona_dymna = Item('zaslona dymna', {'escape_chance': 10})
        konfetti = Item('konfetti', {'escape_chance': 15})

        wytrych = Item('wytrych', {'disarm_chance': 10})
        kaczka = Item('gumowa kaczka', {'disarm_chance': 15})

        self.treasures_pool = {1: [ser, jablko, rekawica, helm, zaslona_dymna, wytrych], 2: [jablko, bandaz, amulet, zbroja, konfetti, wytrych], 3:[bandaz, penicylina, eliksir, deska, kaczka]}

    def enter(self, hero: Hero):
        input("Otwierasz pokoj. Na srodku stoi skrzynia. Nie mozesz jej nie otworzyc. (wcisnij Enter)")
        treasures_dict = {}
        treasures = sample(self.treasures_pool[self.difficulty], k=2)   # losowanie skarbow w skrzyni
        for treasure in treasures:
            print(treasure)
            treasures_dict[treasure.get_name()] = treasure

        while True:
            chosen_treas = input('Ktory skarb wybierasz? ').casefold()
            if chosen_treas in treasures_dict:
                return treasures_dict[chosen_treas]
            else:
                print('Nie ma takiego skarbu. Sprobuj wybrac ponownie.')


class Fight(Room):
    def __init__(self, difficulty):
        super().__init__(difficulty)
        szczur = Enemy('szczur', 30, (5, 10), (5, 10))
        kot = Enemy('kot', 30, (5, 10), (5, 10))
        szkielet = Enemy('szkielet', 15, (10, 20), (10, 15))
        nietoperze = Enemy('zadziwiajaco wielkie nietoperze', 50, (8, 10), (5,10))
        grzyb = Enemy('trujacy grzyb', 25, (10, 20), (5,10))

        goblin = Enemy('goblin', 40, (20, 30), (10, 20))
        zombie = Enemy('zombie dyktator', 40, (5, 10), (40, 50))
        demon = Enemy('niewielki demon', 100, (20, 30), (20, 30))
        mumia = Enemy('mumia', 20, (10, 15), (90, 100))

        nekromanta = Enemy('nekromanta', 100, (10, 20), (45, 50))
        konfiskator = Enemy('konfiskator', 70, (15, 25), (45, 50))
        krolik = Enemy('niepozorny krolik', 40, (50, 100), (5, 10))
        troll = Enemy('troll', 200, (5, 10), (20, 30))

        straznik = Enemy('Straznik Lochu', 200, (10, 20), (50, 60))
    
        self.enemies = {1: [szczur, kot, szkielet, nietoperze, grzyb], 2: [goblin, zombie, demon, mumia], 3: [nekromanta, konfiskator, krolik, troll], 4: [straznik]}

    def enter(self, hero: Hero):
        enemy = choice(self.enemies[self.difficulty])
        self.enemies[self.difficulty] = self.enemies[self.difficulty].remove(enemy)     # cos tu nie dziala
        
        input(f"Otwierasz niepewnie drzwi. Na twojej drodze staje {enemy}. Szykuj sie do walki. (wcisnij Enter)")

        round_nr = 1
        while enemy.life > 0:
            print(f'-------------------- Runda {round_nr} --------------------')
            print(enemy.get_stats())
            enemy_move = enemy.choice()

            if  enemy_move == 'atak':
                attack = enemy.attack()
                defence = 0
                print(f'Planowany ruch przeciwnika: {enemy_move} - {attack}')
            elif enemy_move == 'obrona':
                attack = 0
                defence = enemy.defence()
                print(f'Planowany ruch przeciwnika: {enemy_move} - {defence}')
                
            print()
            print(hero.get_stats())
            hero_move = hero.choice()
            if hero_move == 'atak':
                hero_attack = hero.attack()
                enemy.life -= max(hero_attack - defence, 0)
                print(f'Wykonano {hero_attack} ataku.')

            elif hero_move == 'obrona':
                hero_defence = hero.defence()
                attack -= min(hero_defence, attack)
                print(f'Otrzymano {attack} obrazen.')

            elif hero_move == 'ucieczka':
                if hero.escape_try():
                    return
            
            hero.life -= attack
            if hero.life <= 0:
                hero.life = 0
                return  'game over'
            round_nr += 1
            print()
        print(f'Udalo ci sie pokonac {enemy}!')
        # dodanie przedmiotu z walki


class Trap(Room):
    def enter(self, hero: Hero):
        input("Pokoj wyglada na pusty. Przechodzisz przez niego spokojnie. Slyszysz dziwny zgrzyt pod swoja noga. To pulapka. Probujesz ja rozbroic. (wcisnij Enter)")
        success = choices((True, False), weights=(hero.disarm_chance, 100-hero.disarm_chance), k=1)[0]
        if success:
            print("Udalo ci sie rozbroic pulapke!")
        else:
            print("Tym razem ci sie nie udalo. Dostajesz 10 obrazen.")
            hero.life -= 10 * self.difficulty
            if hero.life <= 0:
                hero.life = 0
                return  'game over'
