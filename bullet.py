import pygame
from settings import bullet_speed,bullet_width,bullet_height,yellow


class Bullet:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.width=bullet_width
        self.height=bullet_height
        self.speed=bullet_speed 
    
    def update(self):
        self.y-=self.speed

    def is_off_screen(self):

        return (self.y+self.height)<0

    def draw(self,screen):
        rect = pygame.Rect(
            self.x-self.width//2,
            self.y-self.height//2,
            self.width,
            self.height
        )       
        pygame.draw.rect(screen,yellow,rect)





