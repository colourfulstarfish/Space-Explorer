import pygame
import settings

def main():
    pygame.init()
    screen=pygame.display.set_mode((settings.width,  settings.height))
    pygame.display.set_caption(settings.title)
    clock=pygame.time.Clock()
    running=True
    while running:
        #draw the game
        screen.fill(settings.black)
        clock.tick(settings.fps)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
