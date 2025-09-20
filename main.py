import pygame
import constants
from player import Player


def main():
    pygame.init()
    clock = pygame.time.Clock()
    delta_time = 0
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    player = Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)

    updatables = []
    drawables = []

    updatables.append(player)
    drawables.append(player)

    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 

        screen.fill(pygame.Color(0,0,0))
        
        for obj in updatables:
            obj.update(delta_time)
        
        for obj in drawables:
            obj.draw(screen)


        pygame.display.flip()
        delta_time = (clock.tick(60))/1000
        
if __name__ == "__main__":
    main()
