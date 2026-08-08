import pygame
import settings

from player import Player

def main():
    pygame.init()
    screen=pygame.display.set_mode((settings.width,  settings.height))
    pygame.display.set_caption(settings.title)
    clock=pygame.time.Clock()

    player=Player(settings.width//2,settings.height//2)    
    bullets=[]

    running=True
    while running:

        for event in pygame.event.get():
            if event.type ==pygame.event.get():
                running=False
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                running=False
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                bullets.append(player.shoot())

        keys=pygame.key.get_pressed()
        player.update(keys)

        for bullet in bullets:
            bullet.update()
        bullets=[b for b in bullets if not b.is_off_screen()]

        #draw the game
        screen.fill(settings.black)
        player .draw(screen)
        for bullet in bullets:
            bullet.draw(screen)
        clock.tick(settings.fps)


        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
    