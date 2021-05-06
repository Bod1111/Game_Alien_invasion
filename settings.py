class Settings():
    """Класс для хронения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Иницилизирует статические настройки игры."""
        self.screen_width = 1200
        self.screen_hieght = 800
        self.bg_color = (230,230,230)

        # Настройка корабля
        self.ships_limit = 3

        # Параметры снаряда
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        # Настройка пришельцев
        self.fleet_drop_speed = 5.0

        # Темп ускорения игры
        self.speedup_scale = 1.1

        # Темп роста стоимости пришельцев
        self.score_scale = 1.5

        self.initialize_dunamic_settings()

    def initialize_dunamic_settings(self):
        """Иницилизирует найстройки, изменяюшиеся в ходе игры."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0
        self.alien_points = 50

        # fleet_direction = 1 обозначет движение вправо, а -1 - влево
        self.fleet_direction = 1

    def increase_speed(self):
        """Увеличивает настройки скорости и стоимости пришельца."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)


