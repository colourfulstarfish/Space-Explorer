import pygame

from settings import (yellow,orange,light_blue,player_width,player_height,player_speed, width, height)
from bullet import Bullet

class Player:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.height=player_height
        self.speed=player_speed
        self.width=player_width

    def update(self,keys):
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y-=self.speed  
        # move back   
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y+=self.speed   
        # move left
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x-=self.speed
        # move right
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x+=self.speed

        # keep the ship on screen.
        if self.y < 0:
            self.y=self.height//2

        if self.y > height:
            self.y=height-(self.height//2)

        if self.x > width:
            self.x=width-(self.width//2)

        if self.x <0:
            self.x=(self.width//2) 

    
    def draw(self, screen):
        cx,cy=self.x ,self.y
        hw=self.width//2
        hh=self.height//2    
        main_body=[
            (cx,cy-hh),
            (cx-hw,cy+hh),
            (cx+hw,cy+hh),
        ]
        pygame.draw.polygon(screen,orange,main_body)

        cockpit=[
                (cx,cy-hh+10),
                (cx-hw//2,cy+hh-10),
                (cx+hw//2,cy+hh-10)
        ]
        pygame.draw.polygon(screen,light_blue,cockpit)

        engine=pygame.Rect(cx-hw//3,cy+hh-6,(hw//3)*2,8)
        pygame.draw.rect(screen,yellow,engine)

    def shoot(self):
        nose_x = self.x
        nose_y=self.y-self.height//2
        return Bullet(nose_x,nose_y)