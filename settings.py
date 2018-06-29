class Settings():
    """klasa przeznaczona dla ustawien gry"""
    def __init__(self):
        """inicjalizacja ustawien"""
        #Ustawienia ekranu
        self.screen_width = 1200
        self.screen_height= 800
        self.bg_color = (230,230,230)
        #ustawienie predkosci statku
        
        #ustawienia pocisku
        
        self.bullet_width =300
        self.bullet_height= 15
        self.bullet_color = 60,60,60
        self.bullets_allowed =3
        #ustawienia obcego
        
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.ship_limit = 3

        self.speedup_scale = 1.1
        self.score_scale = 1.5
        
        
        self.initialize_dynamic_settings()
        
        
    def initialize_dynamic_settings(self):
        """ inicjalizacja ustawien zmienianychw  trakcie gry"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        
        self.feet_direction = 1
        self.alien_points = 50
        
        
    def increse_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print (self.alien_points)
        
        
        
