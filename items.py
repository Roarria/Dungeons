class Item:
    def __init__(self, name: str, stats: dict):
        self.name = name
        self.stats = {}
        for key, value in stats.items():
            self.stats[key] = value

    def get_name(self):
        return self.name

    def __str__(self):          # zmiana napisu - z ang na pl
        stats = ''
        for x, y in self.stats.items():
            if y >= 0:
                stats += f'{x} +{y} '
            else:
                stats += f'{x} {y} '
        
        return f'{self.name}: {stats}'
