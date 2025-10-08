import pygame
import constants
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    delta_time = 0
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)

    score = 0
    font = pygame.font.Font(None, 36)

    player = Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 

        screen.fill(pygame.Color(0,0,0))

        for obj in updatable:
            obj.update(delta_time)
        
        for obj in drawable:
            obj.draw(screen)
        
        for obj in asteroids:
            if obj.checkCollision(player):
                print("Game over!")
                pygame.quit()
                return
            
            for bullet in shots:
                if obj.checkCollision(bullet):
                    score += 1
                    obj.split()
                    bullet.kill()

        display_score = font.render(f"Score: {score}", True, (255,255,255))
        screen.blit(display_score, (20,20))

        pygame.display.flip()
        delta_time = (clock.tick(60))/1000
        
if __name__ == "__main__":
    main()
