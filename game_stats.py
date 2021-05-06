class GameStats():
    """Отслеживание статистики для игры Alien Invasion."""

    def __init__(self,ai_game):
        """Иницилизирует статистику."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Игра Alien Invasion запускается в не активном состоянии.
        self.game_active = False
        # Рекорды не должны сбрасываться
        self.high_score = 0

    def reset_stats(self):
        """Иницилизирует статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.settings.ships_limit
        self.score = 0
        self.level = 1
