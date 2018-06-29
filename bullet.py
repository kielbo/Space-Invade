import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ klasa do zarzadzania pociskami wystrzelonymi przez gracza """
    
    def __init__ (self,ai_settings, screen, ship):
        """utworzenie połozenia pocisku w aktualnym położeniu statku"""
        super(Bullet, self).__init__()
        self.screen = screen
        
        #utworzenie prostokata w punkcie 0.0
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        #Połozenie zdefiniowanie za pomoca wartości zmiennoprzecinkowej
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
    def update(self):
        """ruch pocisuku po ekranie"""
        #aktualizacja polożenia
        self.y -= self.speed_factor
        self.rect.y = self.y
        
    def draw_bullet(self):
        """wyswietlanie pociusku"""
        pygame.draw.rect(self.screen, self.color, self.rect)
        
