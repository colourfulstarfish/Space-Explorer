import pygame

from settings import (yellow,orange,light_blue,player_width,player_height,player_speed, width, height)

class Player:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.height=player_height
        self.speed=player_speed
        self.width=player_width

    def update(self,keys):
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y+=self.speed  
        # move back   
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y-=self.speed   
        # move left
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x-=self.speed
        # move right
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x-=self.speed 
        
        # keep the ship on screen.
        if self.y < 0:
            self.y=self.height//2

        if self.y > height:

            self.y = height-(self.height//2)