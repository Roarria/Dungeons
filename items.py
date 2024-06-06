class Item:
    items = []

    def __init__(self, name = None):
        self.name = name
        self.stats = {}

    def set_stat(self, stat, value):   # wiecej niz jedna stat
        self.stats[stat] = value

    def set_stats(self, new_stats):
        for stat, value in new_stats.items():
            self.set_stat(stat, value)

