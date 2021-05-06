import json

class GameStats():
    """Отслеживание статистики для игры Alien Invasion."""

    def __init__(self,ai_game):
        """Иницилизирует статистику."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Игра Alien Invasion запускается в не активном состоянии.
        self.game_active = False
        # Рекорды не должны сбрасываться
        self.filename = 'high_score.json'
        self.load_high_score()

    def reset_stats(self):
        """Иницилизирует статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.settings.ships_limit
        self.score = 0
        self.level = 1

    def load_high_score(self):
        """Загружает рекорд из файла high_score.json, сли он существует
        иначе создает новый"""
        try:
            with open(self.filename,) as f:
                self.high_score = json.load(f)
        except FileNotFoundError :
            self.high_score = 0
            self.save_high_score()

    def save_high_score(self):
        """Сохранение рекорда"""
        with open(self.filename, 'w') as f:
            json.dump(self.high_score,f)

